from typing import *

from psycopg2 import ProgrammingError

from server.db import connection


class Model:

	__pk__ = None
	__tablename__ = None
	__columns__ = None

	def delete(self):
		cls = self.__class__
		cls.execute_query(
			f"DELETE FROM {cls.__tablename__} WHERE {cls.__pk__} = %s",
			(self.__get_pk(),),
		)

	def insert(self):
		cls = self.__class__
		involved_columns = [c for c in cls.__columns__ if c != cls.__pk__ or self.__get_pk() is not None]

		pk = cls.execute_query(
			f"INSERT INTO {cls.__tablename__}"
			f"({','.join(involved_columns)}) "
			f"values({','.join(['%s']*len(involved_columns))}) "
			f"RETURNING {cls.__pk__}",
			tuple([self.__get_property(column) for column in involved_columns]),
			single=True,
			deserialize=False
		)[0]
		self.__set_property(cls.__pk__, pk)

	def update(self):
		cls = self.__class__
		cls.execute_query(
			f"UPDATE {cls.__tablename__} "
			f"SET {','.join([f'{column} = %s' for column in cls.__columns__])} "
			f"WHERE {cls.__pk__}=%s",
			(
				*[self.__get_property(column) for column in cls.__columns__],
				self.__get_pk()
			),
		)

	def save(self):
		if self.__class__.get_with_pk(self.__get_pk()):
			self.insert()
		else:
			self.update()

	def __get_pk(self):
		return self.__get_property(self.__class__.__pk__)

	def __get_property(self, name):
		return self.__dict__.get(name)

	def __set_property(self, name, value):
		self.__dict__[name] = value

	@classmethod
	def get_all(cls,):
		return cls.execute_query(
			query=f"SELECT {','.join(cls.__columns__)} FROM {cls.__tablename__}",
			args=(),
			single=False
		)

	@classmethod
	def get_with_condition(cls, condition: str, args: Tuple, single=False):
		return cls.execute_query(
			f"SELECT {','.join(cls.__columns__)} FROM {cls.__tablename__} WHERE {condition}",
			args,
			single=single
		)

	@classmethod
	def get_with_pk(cls, pk):
		return cls.get_with_condition(
			f"{cls.__pk__} = %s",
			(pk,),
			single=True
		)

	@classmethod
	def execute_query(cls, query: str, args: Tuple, single=False, deserialize=True):
		print(f"[+]Executing query: {query} with args: {args}")
		cursor = connection.cursor()

		cursor.execute(
			query, args
		)

		connection.commit()

		try:
			if single:
				result = cursor.fetchone()
			else:
				result = cursor.fetchall()
		except ProgrammingError:
			return

		if deserialize:
			return cls._deserialize(result)
		return result

	@classmethod
	def _deserialize(cls, response):
		if response is None:
			return None
		if type(response) == list:
			return [cls(*value) for value in response]
		return cls(*response)

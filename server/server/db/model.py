from server.db import

class Model:

	def __init__(self):
		pass

	@classmethod
	def get_all(cls):

		return cls.__tablename__


	@classmethod
	def _deserialize(cls, response):
		if response is None:
			return None
		if type(response) == list:
			return [cls(*value) for value in response]
		return cls(*response)

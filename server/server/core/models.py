from typing import *

import uuid
from datetime import datetime

from server.db import Model, Serializable


class Request(Model, Serializable):

	__tablename__ = "core_request"
	__columns__ = ("id", "command", "locked", "complete", "start_datetime", "value")
	__pk__ = "id"
	__serialized_fields__ = ("id", "command")

	def __init__(
			self,
			id=None,
			command=None,
			locked=False,
			complete=False,
			start_datetime=None,
			value=None
	):
		self.id = id
		self.command = command
		self.locked = locked
		self.complete = complete
		self.start_datetime = start_datetime
		self.value =value

		if self.id is None:
			self.id = uuid.uuid4()

	@classmethod
	def get_with_complete_and_locked(cls, complete, locked):
		return cls.get_with_condition(
			condition="complete = %s AND locked = %s",
			args=(complete, locked)
		)

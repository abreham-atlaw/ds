import uuid

from server.db import Model


class Token(Model):

	__tablename__ = "auth_token"
	__columns__ = ["id", "token"]
	__pk__ = "id"

	def __init__(self, id=None, token=None):
		self.id = id
		self.token = token

	@classmethod
	def get_by_token(cls, token):
		return Token.get_with_condition("token = %s", (token,), single=True)

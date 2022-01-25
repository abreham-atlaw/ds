from typing import *

from flask import Request


import hashlib

from server import Config
from .models import Token


class Authenticator:

	def __init__(self):
		pass

	def __get_token(self, request: Request) -> str:
		return request.headers.get(Config.AUTH_HEADER_KEY, None)

	def __hash_token(self, token: str) -> str:
		return hashlib.sha512(bytes(token, "utf-8")).hexdigest()

	def authenticate(self, request: Request) -> bool:

		token = self.__get_token(request)
		print("Recieved Token:", token)
		if token is None:
			return False

		hex_digest = self.__hash_token(token)
		result = Token.get_by_token(hex_digest)
		print("Result:", result)
		return result is not None

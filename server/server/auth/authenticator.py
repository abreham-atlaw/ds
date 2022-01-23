from typing import *

from flask import Request
from sqlalchemy.orm import Query

import hashlib
import secrets

from server.db import db
from server import Config
from models import Tokens



class Authenticator:

	def __init__(self):
		pass

	def __get_token(self, request: Request) -> str:
		return request.headers.get(Config.AUTH_HEADER_KEY, None)

	def __hash_token(self, token: str)->str:
		return hashlib.sha512(token).hexdigest()

	def authenticate(self, request: Request) -> bool:

		token = self.__get_token(request)
		if token is None:
			return False

		hex_digest = self.__hash_token(token)

		#query = Query(Tokens, db.session).

		#if(Query(Tokens, db.session)):



from typing import *

from queen.lib.requests import Request
from queen import Config


class ServerRequest(Request):

	def __init__(self, *args, headers=None, **kwargs):
		if headers is None:
			headers = {}
		headers[Config.AUTH_HEADER_KEY] = Config.AUTH_TOKEN
		headers['Content-Type'] = 'application/json'
		super().__init__(*args, headers=headers, **kwargs)


class NewCommandRequest(ServerRequest):

	def __init__(self, command: str):
		super().__init__(
			url=f"{Config.SERVER_HOST}/queen/requests",
			data={
				"command": command
			},
			method=Request.Method.POST
		)


class GetStatusRequest(ServerRequest):

	def __init__(self, request_id):
		super().__init__(
			url=f"{Config.SERVER_HOST}/queen/requests",
			params={
				"id": request_id
			}
		)

	def is_complete(self):
		return self.get_value().get("complete")

	def get_request_value(self):
		return self.get_value().get("value")

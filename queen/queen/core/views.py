from typing import *
from abc import ABC, abstractmethod

from flask import Blueprint, request as flask_request
import json
import time

from .requests import NewCommandRequest, GetStatusRequest
from queen import Config


class View(ABC):

	@abstractmethod
	def handle_post(self):
		pass

	@abstractmethod
	def handle_get(self):
		pass

	def handle(self):

		if flask_request.method == "GET":
			response = self.handle_get()
		else:
			response = self.handle_post()

		return json.dumps(response)


class RequestView(View):

	def __start_command(self, command: str) -> str:
		new_command_request = NewCommandRequest(command)
		new_command_request.call()
		return new_command_request.get_value()

	def __get_command_output(self, request_id: str):

		while True:
			get_status_request = GetStatusRequest(request_id)
			get_status_request.call()
			if get_status_request.is_complete():
				return get_status_request.get_request_value()
			time.sleep(Config.WAIT_TIME)

	def __execute_command(self, command: str):
		request_id: str = self.__start_command(command)
		return self.__get_command_output(request_id)

	def handle_post(self):
		data = flask_request.json
		command = data.get("command")
		return self.__execute_command(command)

	def handle_get(self):
		return "", 405

core_views = Blueprint("core_views", __name__)

request_view = RequestView()


@core_views.route("/", methods=["POST"])
def handle_request():
	return request_view.handle()

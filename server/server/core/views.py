from abc import ABC, abstractmethod

from flask import Blueprint
from flask import request as flask_request

import json
from datetime import datetime

from server.auth import authenticator
from .models import Request


class RequestView(ABC):

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


class AuthorizedRequestView(RequestView, ABC):

	def handle(self):
		if authenticator.authenticate(flask_request):
			return super().handle()
		return "", 403


class WorkerRequestView(RequestView):

	def handle_get(self):
		request: Request = Request.get_with_complete_and_locked(False, False)[0]
		request.locked = True
		request.start_datetime = datetime.now()
		request.update()

		return request.serialize()

	def handle_post(self):
		data = flask_request.json
		print(data)
		request = Request.get_with_pk(data.get("id"))
		request.value = str(data.get("value"))
		request.complete = True
		request.update()
		return "", 200


class QueenRequestView(AuthorizedRequestView):

	def handle_get(self):
		id = flask_request.args.get("id")
		if id is None:
			return [request.serialize() for request in Request.get_all()]
		return Request.get_with_pk(id).serialize()

	def handle_post(self):
		command = flask_request.json.get("command")
		if command is None:
			return "", 400
		request = Request(command=command)
		request.insert()

		return request.id


worker_request_view = WorkerRequestView()
queen_request_view = QueenRequestView()

core_view = Blueprint('core_views', __name__)


@core_view.route("/requests", methods=("GET", "POST"))
def handle_worker_request():
	return worker_request_view.handle()


@core_view.route("/queen/requests", methods=("GET", "POST"))
def handle_queen_request():
	return queen_request_view.handle()

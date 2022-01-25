from typing import *

from flask import Flask, Blueprint

from server import Config
from server import db
from server.core.views import core_view


def setup_app() -> Flask:

	app = Flask(__name__)
	setup_blueprints(app)
	return app


def setup_blueprints(app: Flask):
	blueprints: List[Blueprint] = get_blueprints()
	for blueprint in blueprints:
		app.register_blueprint(blueprint)


def get_blueprints() -> List[Blueprint]:
	return [
		core_view
	]


app: Flask = setup_app()

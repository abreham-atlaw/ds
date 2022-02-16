from typing import *

from flask import Flask, Blueprint
from core.views import core_views


def setup_app() -> Flask:
	app = Flask(__name__)
	return app


def setup_blueprint():
	blueprints = get_blueprints()
	for blueprint in blueprints:
		app.register_blueprint(blueprint)


def get_blueprints() -> List[Blueprint]:
	return [
		core_views
	]


app = setup_app()
setup_blueprint()

from typing import *

import sys


def start(host=None, port=None, debug=None):
	app.run(
		host=host,
		port=port,
		debug=debug
	)


def setup():
	import Config
	sys.path.append(Config.BASE_DIR)


def get_host_and_port() -> tuple[str, str]:
	if len(sys.argv) > 1:
		return tuple(sys.argv[1].split(":"))
	return ("localhost", "8000")


if __name__ == '__main__':

	setup()
	from queen import app
	import queen.Config as Config
	start(*get_host_and_port(), Config.DEBUG)

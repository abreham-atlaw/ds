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


if __name__ == '__main__':

	setup()
	from server import app
	import server.Config as Config
	start("localhost", "8000", Config.DEBUG)
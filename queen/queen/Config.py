import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEBUG = True

AUTH_HEADER_KEY = "AUTH_TOKEN"
ENVIRONMENT_KEY = "QUEEN_AUTH_TOKEN"
AUTH_TOKEN = os.environ.get(ENVIRONMENT_KEY)
SERVER_HOST = "http://localhost:8000"
WAIT_TIME = 5

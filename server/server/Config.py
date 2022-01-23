import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEBUG = True

DATABASE_NAME = "dc_db"
DATABASE_USER = "dc_admin"
DATABASE_PASSWORD = "bGF8ga7w"
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432

AUTH_HEADER_KEY = "AUTH_TOKEN"

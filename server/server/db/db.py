import psycopg2 as pg
import psycopg2.extras

from server import Config

connection = pg.connect(
	dbname=Config.DATABASE_NAME,
	user=Config.DATABASE_USER,
	password=Config.DATABASE_PASSWORD,
	host=Config.DATABASE_HOST,
	port=Config.DATABASE_PORT
)
read_cursor = connection.cursor()

pg.extras.register_uuid()

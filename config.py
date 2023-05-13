import os

class Config(object):

	API_ID = int(os.environ.get("API_ID", ''))	

	BOT_TOKEN = os.environ.get("BOT_TOKEN", '')

	API_HASH = os.environ.get("API_HASH",'')

	DB_URI = os.environ.get("DATABASE_URL", "")

  DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

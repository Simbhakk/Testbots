import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", ''))
	API_HASH = os.environ.get("API_HASH",'')
	BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
	BOT_USERNAME = os.environ.get("BOT_USERNAME", '')
	DB_URI = os.environ.get("DATABASE_URL", "")
  DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")
	

	
	

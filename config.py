import os

class Config(object):

	API_ID = int(os.environ.get("API_ID", ''))	
        DB_URI = os.environ.get("DATABASE_URL", '')
	BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
        DB_NAME = os.environ.get("DATABASE_NAME", '')
	API_HASH = os.environ.get("API_HASH", '')
        

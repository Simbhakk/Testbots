import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", ''))	
        DATABASE_URL = os.environ.get("DATABASE_URL", '')
	BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
        DATABASE_NAME = os.environ.get("DATABASE_NAME", '')
	API_HASH = os.environ.get("API_HASH", '')
        

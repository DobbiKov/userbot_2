
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

api_id = config.get("pyrogram", "api_id")
api_hash = config.get("pyrogram", "api_hash")

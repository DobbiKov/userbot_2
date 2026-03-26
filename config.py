
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

api_id = config.get("pyrogram", "api_id")
api_hash = config.get("pyrogram", "api_hash")
gemini_api = config.get("pyrogram", "gemini_api")
location = config.get("user", "location")

querty_id = 5200613842
me_id = 716720991 


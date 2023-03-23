from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "2929398")
API_HASH = config("API_HASH", "9b0761e56d3d0f89d14563a7e1d29779")
BOT_TOKEN = config("BOT_TOKEN", "5780148364:AAG76KjJtPoa91yxxvvmjujDutJYnrgh8S8")
BOT_UN = config("BOT_UN", "smex_bot_bot")
AUTH_USERS = config("AUTH_USERS", "1602757268")
LOG_CHANNEL = config("LOG_CHANNEL", "SMXLOGS")
LOG_ID = config("LOG_ID", "1968236276")
FORCESUB = config("FORCESUB", "1903834019")
FORCESUB_UN = config("FORCESUB_UN", "DARK_WEB_REBEL")
ACCESS_CHANNEL = config("ACCESS_CHANNEL", "1968236276")
MONGODB_URI = config("MONGODB_URI", "mongodb://musiccbot:musiccbot@12@a96c09c3-260d-44ea-8f73-4a8bfde7e180.musicbottry-7719.mongo.a.osc-fr1.scalingo-dbs.com:30523/musicbottry-7719?replicaSet=musicbottry-7719-rs0&ssl=true")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("2929398", default=None, cast=int)
API_HASH = config("9b0761e56d3d0f89d14563a7e1d29779", default=None)
BOT_TOKEN = config("5780148364:AAG76KjJtPoa91yxxvvmjujDutJYnrgh8S8", default=None)
BOT_UN = config("BOT_UN", "smex_bot_bot")
AUTH_USERS = config("1602757268", default=None, cast=int)
LOG_CHANNEL = config("SMXLOGS", default=None)
LOG_ID = config("1968236276", default=None)
FORCESUB = config("1903834019", default=None)
FORCESUB_UN = config("DARK_WEB_REBEL", "DARK_WEB_REBEL")
ACCESS_CHANNEL = config("1968236276", default=None)
MONGODB_URI = config("MONGODB_URI", default=None)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

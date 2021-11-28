import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "No_Thank_z")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DemonGirlSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DemonGirlUpdate")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a388669f1cd8ef91ba4b9.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "920"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a388669f1cd8ef91ba4b9.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a388669f1cd8ef91ba4b9.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a388669f1cd8ef91ba4b9.jpg")

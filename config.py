import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TELEGRAM_LOCAL_SERVER_URL = os.getenv('TELEGRAM_LOCAL_SERVER_URL')

if TELEGRAM_API_TOKEN is None:
    raise "Set Telegram API token!"
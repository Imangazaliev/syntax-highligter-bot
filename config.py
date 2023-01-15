import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TELEGRAM_LOCAL_SERVER_URL = os.getenv('TELEGRAM_LOCAL_SERVER_URL')
SCREENSHOT_SERVICE_URL = os.getenv('SCREENSHOT_SERVICE_URL')
ROOT_PATH = os.path.dirname(__file__)
LOGS_DIR = ROOT_PATH + "/logs"

if TELEGRAM_API_TOKEN is None:
    raise "Set Telegram API token!"

if SCREENSHOT_SERVICE_URL is None:
    raise "Set screenshot service URL!"

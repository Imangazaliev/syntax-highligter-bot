from aiogram import Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer, TELEGRAM_PRODUCTION
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TELEGRAM_API_TOKEN, TELEGRAM_LOCAL_SERVER_URL

if TELEGRAM_LOCAL_SERVER_URL is None:
    server = TELEGRAM_PRODUCTION
else:
    server = TelegramAPIServer.from_base(TELEGRAM_LOCAL_SERVER_URL)

bot = Bot(token=TELEGRAM_API_TOKEN, server=server)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

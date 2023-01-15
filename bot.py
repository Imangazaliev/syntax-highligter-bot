import logging
import os

from aiogram import executor
from config import LOGS_DIR

from bot.dispatcher import dp
# noinspection PyUnresolvedReferences
import handlers

log_path = LOGS_DIR + "/bot.log"
logging.basicConfig(
    level=logging.INFO,
    filename=log_path,
    filemode="a",
)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

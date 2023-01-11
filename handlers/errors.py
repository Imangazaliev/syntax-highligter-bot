from aiogram import types
from aiogram.utils import exceptions

from bot.dispatcher import dp


@dp.errors_handler(exception=Exception)
async def handle_bot_blocked_error(update: types.Update, exception: Exception):
    ignore_exception_classes = [
        exceptions.BotBlocked,
    ]

    for cls in ignore_exception_classes:
        if isinstance(exception, cls):
            return

    await update.message.reply("Ошибка при обработке запроса.")


@dp.message_handler()
async def handle_unknown_command(message: types.Message):
    await message.answer("Неизвестная команда :(")

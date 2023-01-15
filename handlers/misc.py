from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import requests

from bot.dispatcher import dp
from config import SCREENSHOT_SERVICE_URL


class CodeState(StatesGroup):
    highlight_code = State()


@dp.message_handler(commands=['start', 'help'])
async def handle_start(message: types.Message):
    await message.reply("Бот для подсветки синтаксиса.")


@dp.message_handler(commands=['hl', 'highlight'])
async def handle_hl(message: types.Message):
    await CodeState.highlight_code.set()
    await message.reply("Отправьте сообщение с кодом.")


@dp.message_handler(state=CodeState.highlight_code)
async def handle_hl_response(message: types.Message, state: FSMContext):
    await state.finish()

    params = { "code": message.text }
    response = requests.post(SCREENSHOT_SERVICE_URL + "/generate-image", json=params)

    if response.status_code != 200:
        raise Exception("Error when requesting image:\n" + response.text)

    response_body = response.json()
    media = types.MediaGroup()
    media.attach_photo(types.InputFile(response_body['path']))

    await message.reply_media_group(media)

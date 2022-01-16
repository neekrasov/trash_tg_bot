import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.private import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), Command("set_photo"))
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]  # Фото с самым высоким разрешением
    photo = await photo.download(destination=io.BytesIO())  # BytesIO - сохранение фото в памяти
    input_file = types.InputFile(path_or_bytesio=photo)
    await message.chat.set_photo(
        photo=input_file)  # await bot.set_chat_photo(chat_id=message.chat.chat_id, photo=input_file)


@dp.message_handler(IsGroup(), Command("set_title"))
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await message.chat.set_title(title)


@dp.message_handler(IsGroup(), Command("set_description"))
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    await message.chat.set_description(description)

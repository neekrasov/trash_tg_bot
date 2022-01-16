from aiogram import types

from filters.private import IsPrivate
from handlers.users.base import bot_start
from loader import dp


@dp.message_handler(IsPrivate())
async def polytech_questions(message: types.Message):
    await bot_start(message)


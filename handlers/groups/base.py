from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from filters.private import IsGroup
from loader import dp
from utils.misc import rate_limit


@rate_limit(4)
@dp.message_handler(IsGroup(), CommandStart())
async def bot_help(message: types.Message):
    text = (f"Здравствуйте {message.from_user.full_name}!",
            f"Я бот для администрирования чата.",
            f"Ваш ID: {message.from_user.id}",
            "<b>Список команд представлен в подсказках у администраторов.</b>")
    await message.answer("\n".join(text))

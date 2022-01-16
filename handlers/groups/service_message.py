from filters.private import IsGroup
from loader import dp, bot
from aiogram import types


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    await message.reply(f"Привет,{message.new_chat_members[0].get_mention(as_html=True)}!")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def left_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} вышел из чата")
    elif message.from_user.id == (await bot.me).id:
        await message.answer("Пока-пока!")
    else:
        await message.answer(f"{message.left_chat_member.full_name} был удалён из чата"
                             f"пользователем {message.from_user.get_mention(as_html=True)}.")
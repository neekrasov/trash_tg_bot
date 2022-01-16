import asyncio
import datetime
import re

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters.private import IsGroup, IsAdmin
from loader import dp, bot


@dp.message_handler(IsGroup(), IsAdmin(), Command('ro', prefixes="!/"))
async def read_only(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w +\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if comment == "@Ovia_bot":
        comment = None
    if not time:
        time = 5
    else:
        time = int(time)

    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    if comment:
        service_comment = \
            f"Пользователю {message.reply_to_message.from_user.get_mention(as_html=True)} запрещено писать на {time} минут. По причине : {comment}"
    else:
        service_comment = \
            f"Пользователю {message.reply_to_message.from_user.get_mention(as_html=True)} запрещено писать на {time} минут."

    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_send_polls=False,
        can_change_info=False,
        can_pin_messages=False,
        can_invite_users=False,
    )
    try:
        await bot.restrict_chat_member(user_id=user_id, chat_id=chat_id, permissions=ReadOnlyPermissions,
                                       until_date=until_date)
        await message.answer(service_comment)

    except BadRequest:
        await message.answer(
            f"Пользователь {message.reply_to_message.from_user.get_mention(as_html=True)} является администратором")

    await asyncio.sleep(2)
    await message.delete()


@dp.message_handler(IsGroup(), IsAdmin(), Command('unro', prefixes="!/"))
async def read_only(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_send_polls=True,
        can_change_info=True,
        can_pin_messages=True,
        can_invite_users=True,
    )

    await bot.restrict_chat_member(user_id=user_id, chat_id=chat_id, permissions=ReadOnlyPermissions, until_date=0)
    await message.answer(
        f"Пользователю {message.reply_to_message.from_user.get_mention(as_html=True)} разрешено писать")

    await asyncio.sleep(2)
    await message.delete()


@dp.message_handler(IsGroup(), IsAdmin(), Command('ban', prefixes="!/"))
async def ban_user(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    command_parse = re.compile(r"(!ban|/ban) ?(\d+)? ?([\w +\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if comment == "@Ovia_bot":
        comment = None
    if comment:
        if not time:
            await message.answer(f"Пользователь {message.reply_to_message.from_user.get_mention(as_html=True)} "
                                 f"был забанен.\n"
                                 f"Причина : {comment}")
            await message.chat.kick(user_id)
        else:
            until_date = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
            await message.answer(f"Пользователь {message.reply_to_message.from_user.get_mention(as_html=True)} "
                                 f"был забанен на {time} минут.\n"
                                 f"Причина : {comment}")
            await message.chat.kick(user_id, until_date=until_date)
    else:
        if not time:
            await message.answer(
                f"Пользователь {message.reply_to_message.from_user.get_mention(as_html=True)} был забанен"
            )
            await message.chat.kick(user_id)
        else:
            until_date = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
            await message.answer(f"Пользователь {message.reply_to_message.from_user.get_mention(as_html=True)} "
                                 f"был забанен на {time} минут.\n"
                                 )
            await message.chat.kick(user_id, until_date=until_date)
    await asyncio.sleep(2)
    await message.delete()


@dp.message_handler(IsGroup(), IsAdmin(), Command('unban', prefixes="!/"))
async def unban_user(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    await message.chat.unban(user_id)
    await message.answer(
        f"Пользователь {message.reply_to_message.from_user.get_mention(as_html=True)} был разбанен"
    )

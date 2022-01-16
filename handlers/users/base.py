
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp

from filters.private import IsPrivate
from keyboards.inline.start_keyboard import start_button
from loader import dp
from utils.db_api import quick_commands as db
from utils.misc import rate_limit


@rate_limit(8)
@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    print("base.py")
    await message.answer(
        f"Здравствуйте, {message.from_user.full_name}!\n"
        "Я простой чат-менеджер, который имеет довольно небольшой функционал.\n"
        "Создан исключительно в качестве обучения по разработке telegram-ботов.\n",
        reply_markup=start_button
    )
    await db.add_user(chat_id=message.from_user.id, name=message.from_user.full_name)

@rate_limit(4)
@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = (
        "<b>Основные команды</b>:",
        "/start - начать диалог.",
        "/help - получить справку.\n",
        "<b>Другие команды</b>:",
        "/info_polytech - меню с самыми распространнёными вопросами абитуриентов.<b>(test)</b>",
        "/courses - покупка курсов. <b>(test)</b>",
        "/channels - полезные каналы. <b>(test)</b>",
        "/create_post - предложить пост в канал. <b>(test)</b>",
        "/get_feedback - обратная связь. <b>(test)</b>",
        "/update_email - установить/сменить email . <b>(test)</b>",
        "Так же ты можешь мне переслать несколько сообщений из групп,"
        "а я выведу о них информацию.<b>(test, low information)</b>",
    )

    await message.answer("\n".join(text))


@dp.callback_query_handler(text="help")
async def callback_bot_help(call: types.CallbackQuery):
    await call.answer()
    await bot_help(call.message)


@dp.callback_query_handler(text="code")
async def callback_bot_help(call: types.CallbackQuery):
    await call.answer("Бот временно отсутвует в репозитории.")

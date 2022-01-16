from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from data.config import ADMINS, channels
from filters.private import IsPrivate
from keyboards.inline.confirm_post import confirm_post_button, callback_post
from loader import dp
from states.poster import NewPost


@dp.message_handler(IsPrivate(), Command("create_post"))
async def create_post(message: types.Message):
    await message.answer("Отправьте мне текст вашего поста, для публикации")
    await NewPost.enter_message.set()


@dp.message_handler(state=NewPost.enter_message)
async def enter_message(message: types.Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("Вы собираетесь отправить пост на проверку?", reply_markup=confirm_post_button)
    await NewPost.next()


@dp.callback_query_handler(callback_post.filter(action="post"), state=NewPost.confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = data.get("text")
    mention = data.get("mention")
    # async with state.proxy() as data:
    #     text = data.get("text")
    #     mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()  # close keyboard
    await call.message.answer("Вы отправили пост на проверку..")
    await dp.bot.send_message(chat_id=ADMINS[0], text=f"Пользователь {mention} подал заявку на публикацию поста")
    await dp.bot.send_message(chat_id=ADMINS[0], text=text, parse_mode="HTML", reply_markup=confirm_post_button)


@dp.callback_query_handler(callback_post.filter(action="cancel"), state=NewPost.confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.answer("Вы отклонили пост", show_alert=True)


@dp.message_handler(IsPrivate(), state=NewPost.confirm)
async def _post_flood(message: types.Message):
    await message.answer("Выберите опубликовать или отклонить пост.")


@dp.callback_query_handler(callback_post.filter(action="post"), user_id=ADMINS[0])
async def approve_post(call: CallbackQuery):
    await call.answer("Пост успешно опубликован", show_alert=True)
    target_channel = channels[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(callback_post.filter(action="cancel"), user_id=ADMINS[0])
async def confirm_post(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer("Вы отклонили публикацию поста", show_alert=True)

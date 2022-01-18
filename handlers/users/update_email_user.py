from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline.set_email import cancel_email
from loader import dp
from utils.db_api import db_commands as db


@dp.message_handler(Command("update_email"))
async def add_email(mesage: types.Message, state: FSMContext):
    await mesage.answer("В ожидании отправки email...", reply_markup=cancel_email)
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    await db.update_email(chat_id=message.from_user.id, email=message.text)
    await message.answer(f"Ваш email был обновлен на <b>{message.text}</b>")
    await state.finish()


@dp.callback_query_handler(text="cancel", state="email")
async def cancel_update_email(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Вы отменили изменение email.", show_alert=True, )
    await state.finish()

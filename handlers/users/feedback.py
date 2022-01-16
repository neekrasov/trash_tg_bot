from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.get_callback import callback
from loader import dp


@dp.message_handler(Command('get_feedback'))
async def get_feedback(message: types.Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}!\n"
                         f"Для того, чтобы связаться с менеджером оставьте свои контактные данные"
                         f"(электронная почта или номер телефона).\n"
                         f"Сделать вы это можете нажав на кнопки ниже.", reply_markup=callback)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def send_mail(message: types.Message):
    contact = message.contact
    await message.answer(f"Спасибо {contact.full_name}\n"
                         f"Ваш номер {contact.phone_number} был получен и передан менеджеру.",
                         reply_markup=ReplyKeyboardRemove())
    await dp.bot.send_message(chat_id=ADMINS[0], text="Заявка на получение обратной связи от пользователя"
                                                      f"{message.from_user.get_mention()} по номеру телефона:"
                                                      f"{contact.phone_number}")


@dp.message_handler(text="📩")
async def send_mail(message: types.Message, state: FSMContext):
    await message.answer("Пожалуйста введите электронную почту:")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_message(message: types.Message, state: FSMContext):
    await state.update_data(mail=message.text)
    dataset = await state.get_data()
    await state.finish()
    await message.answer("Заявка успешно отправлена..")
    await dp.bot.send_message(chat_id=ADMINS[0],
                              text=f"Пользователь {message.from_user.get_mention()} подал заявку "
                                   f"на получение обратной связи по электронной почте : {dataset.get('mail')}",
                              reply_markup=ReplyKeyboardRemove())

# Достать дату
# await state.update_data(answer1=answer)
#
# # await state.update_data(
# #     {
# #         "answer1": answer
# #     }
# # )
#
# #
# async with state.proxy() as data:
#     data["answer1"] = answer

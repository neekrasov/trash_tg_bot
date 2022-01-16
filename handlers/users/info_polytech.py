from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from filters.private import IsPrivate
from keyboards.default import menu_keyboard
from loader import dp


@dp.message_handler(IsPrivate(), Command("info_polytech"))
async def show_menu(message: types.Message):
    await message.answer("Здравствуйте! Выберите информацию которая вам интересна.", reply_markup=menu_keyboard.menu)


@dp.message_handler(text="Проходные баллы")
async def button1(message: types.Message):
    await message.answer("Информация по поводу проходных баллов прошлых лет: \n"
                         "https://mospolytech.ru/postupayushchim/priem-v-universitet/prohodnye-bally/")


@dp.message_handler(Text(equals=['Программы обучения']))
async def button2(message: types.Message):
    await message.answer("Информация по поводу программ обучения:\n"
                         "https://mospolytech.ru/postupayushchim/programmy-obucheniya/")


@dp.message_handler(Text(equals=['Факультеты и институты']))
async def button2(message: types.Message):
    await message.answer("Информация о всех институтах:\n"
                         "https://mospolytech.ru/fakultety-i-instituty/")


@dp.message_handler(Text(equals=['Стоимость обучения']))
async def button2(message: types.Message):
    await message.answer("Информация по поводу стоимости обучения:\n"
                         "https://mospolytech.ru/postupayushchim/priem-v-universitet/stoimost-obucheniya/")


@dp.message_handler(Text(equals=['Проектная деятельность']))
async def button2(message: types.Message):
    await message.answer("Информация по поводу проектной деястельности:\n"
                         "https://mospolytech.ru/obuchauschimsya/proektnaya-deyatelnost/")


@dp.message_handler(Text(equals=['Студенческий городок']))
async def button2(message: types.Message):
    await message.answer("Информация о студенческом городке:\n"
                         "https://mospolytech.ru/obschejitiya/")


@dp.message_handler(Text(equals=['Отмена выбора']))
async def button3(message: types.Message):
    await message.answer("Вы отменили выбор.", reply_markup=ReplyKeyboardRemove())


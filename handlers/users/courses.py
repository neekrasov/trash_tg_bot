from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from filters.private import IsPrivate
from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.buy_corses import buy, buy_course_keyboard, more
from loader import dp


@dp.message_handler(IsPrivate(), Command('courses'))
async def show_items(message: types.Message):
    await message.answer("Чтобы приобрести желаемый курс по одному"
                         " из представленных языков программирования и фреймворков,"
                         "нажмите на кнопку с нужным товаром.", reply_markup=buy_course_keyboard)


@dp.callback_query_handler(buy_callback.filter(course='Python'))
async def buying_python(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)  # await bot.answer_callback_query(callback_query_id=call.chat_id)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по Python, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(buy_callback.filter(course='Java'))
async def buying_java(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по Java, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(buy_callback.filter(course='C++'))
async def buying_java(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по C++, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(buy_callback.filter(course='C#'))
async def buying_java(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по C#, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(buy_callback.filter(course='JS+HTML+CSS'))
async def buying_java(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по JS+HTML+CSS, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(buy_callback.filter(course='Python+Django'))
async def buying_java(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по Python+Django, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(buy_callback.filter(course='JS+Vue.js'))
async def buying_java(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по JS+Vue.js, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(buy_callback.filter(course='Python+Django'))
async def buying_java(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    count = callback_data.get("count")
    await call.message.answer(f"Хотите приобрести курс по Python+aiohttp, в количестве {count}шт?\n"
                              f"Чтобы получить его нажмите на кнопку.", reply_markup=buy)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer(f"Вы отменили выбор.", show_alert=True)
    await call.message.delete_reply_markup()


@dp.callback_query_handler(text="more")
async def cancel(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Дополнительные курсы: ", reply_markup=more)


@dp.callback_query_handler(buy_callback.filter(course="test"))
async def cancel(call: CallbackQuery):
    await call.answer("К сожалению дополнительных курсов нет.", show_alert=True)
    # await call.message.delete_reply_markup()

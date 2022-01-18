from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from keyboards.inline.menu_keyboard import categories_keyboard, subcategories_keyboard, items_keyboard, item_keyboard, \
    menu_cd
from loader import dp
from utils.db_api.db_commands import get_item


@dp.message_handler(IsPrivate(), Command("menu"))
async def show_menu(message: types.Message):
    await list_categories(message)


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        await message.answer("Смотрите, что у нас есть", reply_markup=markup)
    if isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def list_subcategories(call: types.CallbackQuery, category,
                             **kwargs):  # **kwargs - летят подкатегории, айтем айди и тп
    markup = await subcategories_keyboard(category)
    await call.message.edit_reply_markup(markup)


async def list_items(call: types.CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)
    await call.message.edit_text("Смотрите что у нас есть", reply_markup=markup)


async def show_item(call: types.CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)
    item = await get_item(item_id)
    text = f"Покупка {item}"
    await call.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get("level")
    category = callback_data.get("category")
    subcategory = callback_data.get("subcategory")
    item_id = callback_data.get("item_id")

    levels = {
        "0": list_categories,
        "1": list_subcategories,
        "2": list_items,
        "3": show_item,
    }

    current_level_function = levels[current_level]
    await current_level_function(call, category=category, subcategory=subcategory, item_id=item_id)

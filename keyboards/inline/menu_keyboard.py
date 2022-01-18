from unicodedata import category

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from utils.db_api.db_commands import get_categories, count_items, get_subcategories, get_items

menu_cd = CallbackData("show_menu", "level", "category", "subcategory", "item_id")
buy_item = CallbackData("buy", "item_id")


def make_callback_data(level, category="0", subcategory="0", item_id="0"):
    return menu_cd.new(
        level=level,
        category=category,
        subcategory=subcategory,
        item_id=item_id
    )


async def categories_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()

    categories = await get_categories()
    for category in categories:
        numer_of_item = await count_items(category.category_code)
        text_button = f"{category.category_name} ({numer_of_item})"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category.category_code)
        markup.insert(
            InlineKeyboardButton(text=text_button, callback_data=callback_data)
        )
    return markup


async def subcategories_keyboard(category_code):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    subcategories = await get_subcategories(category_code)
    for subcategory in subcategories:
        numer_of_item = await count_items(category_code=category_code, subcategory_code=subcategory.subcategory_code)
        text_button = f"{subcategory.subcategory_name} ({numer_of_item})"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           subcategory=subcategory.subcategory_code)
        markup.insert(
            InlineKeyboardButton(text=text_button, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup


async def items_keyboard(category_code, subcategory_code):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)

    items = await get_items(category_code=category_code, subcategory_code=subcategory_code)
    for item in items:
        text_button = f"{item.name} - ₱{item.price}"
        callback_data = make_callback_data(level=CURRENT_LEVEL,
                                           category=category_code,
                                           subcategory=subcategory_code,
                                           item_id=str(item.id))
        markup.insert(
            InlineKeyboardButton(text=text_button, callback_data=callback_data)
        )
        markup.row(
            InlineKeyboardButton(
                text="Назад",
                callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                                 category=category_code)
            )
        )
    return markup


def item_keyboard(category, subcategory, item_id):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text="Купить",
                             callback_data=buy_item.new(item_id)
                             )
    )
    markup.row(
        InlineKeyboardButton(text="Назад",
                             callback_data=make_callback_data(level=CURRENT_LEVEL - 1,
                                                              category=category,
                                                              subcategory=subcategory)
                             )
    )
    return markup

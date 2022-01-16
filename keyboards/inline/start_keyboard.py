from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить справку", callback_data='help'),
            InlineKeyboardButton(text="Исходники", callback_data='code'),
        ]
    ])

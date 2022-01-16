from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_email = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text="Отмена", callback_data="cancel")
    ]
])
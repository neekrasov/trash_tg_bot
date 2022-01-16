from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

callback = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="📲", request_contact=True),
        KeyboardButton(text="📩")
    ]
], resize_keyboard=True)

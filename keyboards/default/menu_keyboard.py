from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Проходные баллы'),
            KeyboardButton(text='Программы обучения'),
        ],
        [
            KeyboardButton(text='Факультеты и институты'),
            KeyboardButton(text='Стоимость обучения'),

        ],
        [
            KeyboardButton(text='Проектная деятельность'),
            KeyboardButton(text='Студенческий городок'),
        ],
        [
            KeyboardButton(text='Отмена выбора'),
        ]
    ],
    resize_keyboard=True
)

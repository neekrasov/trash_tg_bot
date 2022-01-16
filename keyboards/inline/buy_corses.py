from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

buy_course_keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="'Java'-course",
            callback_data=buy_callback.new(
                course='Java',
                count=1,
            ),
        ),
        InlineKeyboardButton(
            text="'Python'-course",
            callback_data=buy_callback.new(
                course='Python',
                count=1,
            ),
        )
    ],

    [
        InlineKeyboardButton(
            text="'C++'-course",
            callback_data=buy_callback.new(
                course='C++',
                count=1,
            ),
        ),
        InlineKeyboardButton(
            text="'C#'-course",
            callback_data=buy_callback.new(
                course='C#',
                count=1,
            ),
        )
    ],
    [
        InlineKeyboardButton(
            text="'JS+HTML+CSS'-course",
            callback_data=buy_callback.new(
                course='JS+HTML+CSS',
                count=1,
            ),
        ),
        InlineKeyboardButton(
            text="'Python+Django'-course",
            callback_data=buy_callback.new(
                course='Python+Django',
                count=1,
            ),
        )
    ],
    [
        InlineKeyboardButton(
            text="'JS+Vue.js'- course",
            callback_data=buy_callback.new(
                course='JS+Vue.js',
                count=1,
            ),
        ),
        InlineKeyboardButton(
            text="'Python+aiohttp'- course",
            callback_data=buy_callback.new(
                course='C++',
                count=1,
            ),
        )
    ],
    [
        InlineKeyboardButton(
            text='Cancel',
            callback_data='cancel'
        )
    ],
    [
        InlineKeyboardButton(
            text='More',
            callback_data='more'
        )
    ],
])

buy = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="tipo link na course, no na site polytech", url="https://mospolytech.ru/"),
        InlineKeyboardButton(text="Cancel", callback_data="cancel")
    ]
])

more = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="тут могли быть доп. курсы",
            callback_data=buy_callback.new(
                course='test',
                count=1,
            ),
        ),
        InlineKeyboardButton(
            text="и тут",
            callback_data=buy_callback.new(
                course='test',
                count=1,
            ),
        )
    ],
    [
        InlineKeyboardButton(text='Cancel', callback_data='cancel')
    ]

])

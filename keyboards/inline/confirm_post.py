from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback_post = CallbackData("create_post", "action")

confirm_post_button = InlineKeyboardMarkup(row_width=2,
                                           inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(text="Да",
                                                                        callback_data=callback_post.new(action="post"))
                                               ],
                                               [
                                                   InlineKeyboardButton(text="Нет",
                                                                        callback_data=callback_post.new(
                                                                            action="cancel"))
                                               ]
                                           ]
                                           )

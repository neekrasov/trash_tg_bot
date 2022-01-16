from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    enter_message = State()
    confirm = State()
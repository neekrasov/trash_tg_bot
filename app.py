from aiogram import executor

from handlers import dp
import middlewares, filters, handlers
from utils.db_api import database_gino
from utils.db_api.database_gino import db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    filters.setup(dp)
    middlewares.setup(dp)
    await database_gino.on_startup(dp)  # connect to bd
    await db.gino.create_all()  # create_tables
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


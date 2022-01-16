import asyncpg

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(chat_id: int, name: str, email: str = None):
    try:
        user = User(chat_id=chat_id, name=name, email=email)
        await user.create()
    except asyncpg.exceptions.UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(chat_id: int):
    user = await User.query.where(User.chat_id == chat_id).gino.first()  # select first string
    return user


async def count_users():
    count = await db.func.count(User.chat_id).gino.scalar()  # select first value
    return count


async def update_email(chat_id: int, email: str):
    user = await User.get(chat_id=chat_id)
    await user.update(email=email).apply()


async def delete_users():
    users = await User.query.gino.all()
    await users.delete().apply()


async def delete_user(chat_id: int):
    user = await User.get(pk=chat_id)
    await user.delete().apply()

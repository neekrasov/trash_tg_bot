from typing import List

import asyncpg
from sqlalchemy import and_

from utils.db_api.database_gino import db
from utils.db_api.models import User, Item

""" Users quick commands"""


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


""" Items quick commands"""


async def add_item(**kwargs):
    item = await Item(**kwargs).create()  # create new item
    return item


async def get_categories() -> List[Item]:
    command = await Item.query.distinct(Item.category_code).gino.all()
    print(f'get_categories:{command}')
    return await Item.query.distinct(Item.category_code).gino.all()


async def get_subcategories(category_code) -> List[Item]:
    return await Item.query.distinct(Item.subcategory_code).where(Item.category_code == category_code).gino.all()


async def count_items(category_code, subcategory_code=None):
    conditions = [Item.category_code == category_code]

    if subcategory_code:
        conditions.append(Item.subcategory_code == subcategory_code)

    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()  # get degree
    return total


async def get_items(category_code, subcategory_code) -> List[Item]:
    items = await Item.query.where(
        and_(Item.category_code == category_code,
             Item.subcategory_code == subcategory_code)
    ).gino.all()
    print(f"get_items: {items}")
    return items


async def get_item(item_id) -> Item:
    item = await Item.query.where(Item.id == item_id).gino.first()
    return item

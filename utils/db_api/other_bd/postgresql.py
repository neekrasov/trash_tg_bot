# from typing import Union
#
# import asyncpg
# from asyncpg.pool import Pool
#
# from data import config
#
# class Database:
#     def __init__(self):
#         """ Создаётся база данных для подключения в loader"""
#
#         self.pool: Union[Pool, None] = None  # Union[может быть таким, или таким]
#
#     async def create(self):
#         """ Подключение к базе данных """
#
#         pool = await asyncpg.create_pool(
#             user=config.PGUSER,
#             password=config.PGPASSWORD,
#             host=config.IP,
#             # database = config.DATABASE
#         )
#
#         self.pool = pool
#
#     async def create_table_users(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS Users(
#             chat_id BIGINTа NOT NULL,
#             name varchar(255) NOT NULL,
#             email varchar(255),
#             PRIMARY KEY (chat_id)
#         );
#         """
#         await self.pool.execute(sql)
#
#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join([
#             f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
#         ])
#         return sql, tuple(parameters.values())
#
#     async def add_user(self, chat_id: int, name: str, email: str = None):
#         sql = "INSERT INTO Users (chat_id, name, email) VALUES ($1, $2, $3)"
#         try:
#             await self.pool.execute(sql, chat_id, name, email)
#         except asyncpg.exceptions.UniqueViolationError:
#             pass
#
#     async def select_all_users(self):
#         sql = "SELECT * FROM Users "
#         return await self.pool.fetch(sql)  # many strings
#
#     async def select_user(self, parameters: dict):
#         sql = "SELECT * FROM Users WHERE "
#         sql, parameters = self.format_args(sql, parameters)
#         return await self.pool.fetchrow(sql, *parameters)  # one string
#
#     async def count_users(self):
#         return await self.pool.fetchval("SELECT COUNT(*) FROM Users")  # one value
#
#     async def update_email(self, email, chat_id):
#         sql = "UPDATE Users SET email = $1 WHERE chat_id = $2 "
#         return await self.pool.execute(sql, email, chat_id)
#
#     async def delete_users(self):
#         await self.pool.execute("DELETE FROM Users WHERE True")
#
#     async def delete_user(self, chat_id):
#         await self.pool.execute("DELETE FROM Users WHERE chat_id = $1", chat_id)
#
#
# def logger(statement):
#     print(f"""
#     -------------------------------------------------------------------------
#     Executing:
#     {statement}
#     -------------------------------------------------------------------------
#     """)
# import sqlite3
#
#
# class Database:
#     def __init__(self, path_to_db="data/users_data.db"):
#         self.path_to_db = path_to_db
#
#     @property
#     def connection(self):
#         return sqlite3.connect(self.path_to_db)
#
#     def execute(self, sql: str, params: tuple = None, fetchone=False, fetchall=False, commit=False):
#
#         """
#         sql - INSERT INTO User (chat_id, name, email) VALUES(?,?,?)
#
#         params -
#
#         fetchone -
#
#         fetchall -
#
#         commit -
#
#         """
#         if not params:
#             params = tuple()
#         connection = self.connection
#
#         connection.set_trace_callback(logger)  # Активация логов
#
#         cursor = connection.cursor()
#
#         cursor.execute(sql, params)
#
#         data = None
#
#         if commit:
#             connection.commit()
#
#         if fetchone:
#             data = cursor.fetchone()
#
#         if fetchall:
#             data = cursor.fetchall()
#         connection.close()
#
#         return data
#
#     def create_table_users(self):
#         sql = """
#         CREATE TABLE Users (
#         chat_id int NOT NULL ,
#         name varchar(255) NOT NULL,
#         email varchar(255),
#         PRIMARY KEY (chat_id)
#         );
#         """
#
#         self.execute(sql, commit=True)
#
#     def add_user(self, chat_id: int, name: str, email: str = None):
#         sql = "INSERT INTO Users(chat_id, name, email) VALUES (?, ?, ?)"
#         params = (chat_id, name, email)
#         self.execute(sql=sql, params=params, commit=True)
#
#     def select_all_users(self):
#         sql = "SELECT * FROM Users"
#         return self.execute(sql, fetchall=True)
#
#     @staticmethod
#     def format_args(sql, params: dict):
#         sql += " AND ".join([
#             f"{item} = ?" for item in params
#         ])
#         return sql, tuple(params.values())
#
#     def select_user(self, **kwargs):
#         sql = "SELECT * FROM Users WHERE "
#         sql, params = self.format_args(sql, kwargs)
#         return self.execute(sql, params, fetchone=True)
#
#     def count_users(self):
#         return self.execute(sql="SELECT COUNT(*) FROM Users;", fetchone=True)
#
#     def update_email(self, email, chat_id):
#         sql = "UPDATE Users SET email = ? WHERE chat_id = ?"
#         return self.execute(sql=sql, params=(email, chat_id), commit=True)
#
#     def delete_all_users(self):
#         self.execute("DELETE FROM Users WHERE True", commit=True)
#
#     def delete_user(self, chat_id):
#         self.execute("DELETE FROM Users WHERE chat_id = ?", params=(chat_id), commit=True)
#
#
# def logger(statement):
#     print(f"""
#     -------------------------------------------------------------------------
#     Executing:
#     {statement}
#     -------------------------------------------------------------------------
#     """)

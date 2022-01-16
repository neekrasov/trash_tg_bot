from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    chat_id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

    referral = Column(BigInteger)

    query: sql.Select

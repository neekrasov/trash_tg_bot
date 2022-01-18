from sqlalchemy import Column, BigInteger, String, sql, Integer, Sequence

from utils.db_api.database_gino import TimedBaseModel, db


class User(TimedBaseModel):
    __tablename__ = 'users'
    chat_id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

    referral = Column(BigInteger)

    query: sql.Select


class Item(db.Model):
    __tablename__ = "items"
    query: sql.Select

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    category_code = Column(String(20))
    category_name = Column(String(50))

    subcategory_code = Column(String(20))
    subcategory_name = Column(String(50))

    name = Column(String(50))
    photo = Column(String(250))
    price = Column(Integer)

    def __repr__(self):
        return f"""
        Product №{self.id} - {self.name}
        Price: {self.price}
        """

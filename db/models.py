from sqlalchemy import VARCHAR, Column, Boolean, TIMESTAMP, Integer
from db.connection import Base


class users(Base):
    __tablename__ = "users"

    user_id = Column(VARCHAR(45), primary_key=True, nullable=False)
    email = Column(VARCHAR(45), nullable=False,unique=True)
    pwd = Column(VARCHAR(45), nullable=False)
    status = Column(Boolean, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False)


class account_book(Base):
    __tablename__ = "account_book"

    no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(VARCHAR(45), nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(VARCHAR(45), nullable=False)
    memo = Column(VARCHAR(45), nullable=False)
    status = Column(Boolean, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False)

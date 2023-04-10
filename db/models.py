from sqlalchemy import VARCHAR, Column, Boolean, TIMESTAMP, Integer, Date
from sqlalchemy.orm import validates
from db.connection import Base
from datetime import datetime
import re


class users(Base):
    __tablename__ = "users"

    user_id = Column(VARCHAR(255), primary_key=True, nullable=False)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    pwd = Column(VARCHAR(255), nullable=False)
    status = Column(Boolean, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False)

    @validates('user_id')
    def validate_user_id(self, key, value):
        if not re.match("^[a-z0-9_-]{5,20}$", value):
            raise ValueError("5~20자의 영문 소문자, 숫자와 특수기호(_),(-)만 사용 가능합니다.")

        return value

    @validates('email')
    def validate_email(self, key, value):
        if not re.match("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            raise ValueError("이메일 형식이 아닙니다.")

        return value


class account_book(Base):
    __tablename__ = "account_book"

    no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(VARCHAR(45), nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    memo = Column(VARCHAR(45), nullable=False)
    status = Column(Boolean, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False)

    @validates('date')
    def validate_date(self, key, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return value

        except ValueError:
            raise ValueError("날짜는 YYYYY-MM-DD 형식만 가능합니다")

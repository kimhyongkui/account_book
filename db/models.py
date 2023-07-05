from fastapi import status, HTTPException
from sqlalchemy import VARCHAR, Column, Boolean, TIMESTAMP, Integer, Date
from sqlalchemy.orm import validates
from db.connection import Base
from datetime import datetime
import re


class Users(Base):
    __tablename__ = "users"

    user_id = Column(VARCHAR(50), primary_key=True, nullable=False)
    email = Column(VARCHAR(50), nullable=False, unique=True)
    pwd = Column(VARCHAR(100), nullable=False)
    status = Column(Boolean, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False)

    @validates('user_id')
    def validate_user_id(self, key, value):
        if not re.match("^[a-z0-9_-]{5,20}$", value):
            raise ValueError("5~20자의 영문 소문자, 숫자와 특수기호(_),(-)만 사용 가능합니다.")

        return value

    @validates('email')
    def validate_email(self, key, value):
        if len(value) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="이메일 주소가 너무 깁니다. 50자를 넘지 말아주세요.")

        if not re.match("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            raise ValueError("이메일 형식이 아닙니다.")

        return value

    @validates('pwd')
    def validate_memo(self, key, value):
        if len(value) > 100:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="비밀번호가 너무 깁니다. 100자를 넘지 말아주세요.")

        return value


class Account_book(Base):
    __tablename__ = "account_book"

    no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(VARCHAR(50), nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    memo = Column(VARCHAR(255), nullable=False)
    status = Column(Boolean, nullable=False)
    create_time = Column(TIMESTAMP, nullable=False)

    @validates('amount')
    def validate_amount(self, key, value):
        if type(value) != int:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="숫자만 사용 할 수 있습니다.")

        return value

    @validates('date')
    def validate_date(self, key, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return value

        except ValueError:
            raise ValueError("날짜는 YYYYY-MM-DD 형식만 가능합니다")

    @validates('memo')
    def validate_memo(self, key, value):
        if len(value) > 255:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="메모가 너무 깁니다. 255자를 넘지 말아주세요.")

        return value

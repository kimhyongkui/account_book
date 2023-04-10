from fastapi import HTTPException, status
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime, timedelta
from jose import jwt
from app.auth import verify_password
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

Session = sessionmaker(bind=engine)
session = Session()


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def login(user_id, pwd):
    try:
        user = session.query(users).filter_by(user_id=user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="아이디 또는 메일을 확인하세요.")

        if not verify_password(pwd, user.pwd):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="비밀번호가 틀렸습니다.")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"user_id": user.user_id},
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer", "user_id": user.user_id}

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

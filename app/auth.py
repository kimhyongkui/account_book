from fastapi import Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/account-book/login")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

SessionLocal = sessionmaker(bind=engine)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def password_hash(pwd):
    return bcrypt_context.hash(pwd)


def verify_password(pwd, hashed_password):
    return bcrypt_context.verify(pwd, hashed_password)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="인증된 권한이 없습니다")

        return user_id

    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="인증된 권한이 없습니다")

from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
from db.create.logout import blacklist
from datetime import datetime
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


def get_user_auth(token: str = Depends(oauth2_scheme)):
    try:
        if token in blacklist:
            raise HTTPException(status_code=400, detail="취소된 토큰입니다")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        timestamp = datetime.utcfromtimestamp(payload["exp"])
        if timestamp < datetime.utcnow():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="만료된 토큰")

        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="인증된 권한이 없습니다.")

        return user_id

    except HTTPException as err:
        raise err

    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="인증된 권한이 없습니다.")

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from passlib.context import CryptContext
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/account-book/login")

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

SessionLocal = sessionmaker(bind=engine)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        else:
            return user_id
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


def password_hash(pwd):
    return bcrypt_context.hash(pwd)


def verify_password(pwd, hashed_password):
    return bcrypt_context.verify(pwd, hashed_password)

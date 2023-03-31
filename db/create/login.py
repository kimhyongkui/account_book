from fastapi import HTTPException, status
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from passlib.context import CryptContext
from jwt import encode, decode
import os

Session = sessionmaker(bind=engine)
session = Session()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def create_token(user_id):
    token_data = {"sub": user_id}
    return encode(token_data, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token):
    try:
        return decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return None


def login_user(user_id, pwd):
    try:
        user = session.query(users).filter_by(user_id=user_id).first()
        if not user or not bcrypt_context.verify(pwd, user.pwd):
            return None

        token = create_token(user_id)
        session.query(users).filter_by(user_id=user_id, status=True, permission=False). \
            update({"permission": True, "create_time": datetime.now()})
        session.commit()

        return token

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


def logout_user(user_id):
    try:
        user = session.query(users).filter_by(user_id=user_id, permission=True).first()
        if not user:
            return False
        session.query(users).filter_by(user_id=user_id, status=True, permission=True). \
            update({"permission": False})
        session.commit()
        return True

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()

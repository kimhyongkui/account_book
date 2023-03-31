from fastapi import HTTPException, status, Header
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from passlib.context import CryptContext
from jwt import encode, decode, InvalidTokenError
import os

Session = sessionmaker(bind=engine)
session = Session()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def create_token(user_id):
    token_data = {"sub": user_id}
    return encode(token_data, SECRET_KEY, algorithm=ALGORITHM)


def authenticate_user(token: str = Header(...)):
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        user = session.query(users).filter_by(user_id=user_id, permission=True).first()
        if user:
            return user_id
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")


def login_user(user_id, pwd):
    try:
        user = session.query(users).filter_by(user_id=user_id).first()
        if not user or not bcrypt_context.verify(pwd, user.pwd):
            result = JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "틀린 아이디 또는 이메일"})
        else:
            token = create_token(user_id)

            session.query(users).filter_by(user_id=user_id, status=True, permission=False). \
                update({"permission": True, "create_time": datetime.now()})
            session.commit()
            result = {"access_token": token, "token_type": "bearer"}
        return result
    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


def logout_user(user_id):
    try:
        session.query(users).filter_by(user_id=user_id, status=True, permission=True). \
            update({"permission": False})
        session.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "로그아웃 성공"})

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_INTERNAL_SERVER_ERROR, detail=str(err))
    finally:
        session.close()



from fastapi import APIRouter, Depends
from db.models import users
from db.connection import engine
from sqlalchemy.orm import sessionmaker
from fastapi import status
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from datetime import datetime
from app.auth import has_permission


Session = sessionmaker(bind=engine)
session = Session()

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


@router.post('/login', tags=["login"])
def login(user_id: str, pwd: str):
    try:
        user = session.query(users).filter_by(user_id=user_id, status=True).first()
        if not user:
            result = JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "아이디가 없습니다"})

        elif not bcrypt_context.verify(pwd, user.pwd):
            result = JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "비밀번호가 틀립니다"})

        else:
            session.query(users).filter_by(user_id=user_id, status=True).\
                update({"permission": True, "create_time": datetime.now()})
            session.commit()
            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "로그인 성공"})

        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()


@router.post('/logout', tags=["logout"])
def logout(user_id: str = Depends(has_permission)):
    try:
        session.query(users).filter_by(user_id=user_id, status=True). \
            update({"permission": False, "create_time": datetime.now()})
        session.commit()
        result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "로그아웃 성공"})
        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

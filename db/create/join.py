from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse
from passlib.context import CryptContext

Session = sessionmaker(bind=engine)
session = Session()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def create_account(user_id, email, pwd):
    try:
        check_id = session.query(users).filter_by(user_id=user_id).first()
        check_email = session.query(users).filter_by(email=email).first()
        if check_id or check_email:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "이미 존재하는 아이디 또는 이메일입니다."})

        hashed_pwd = bcrypt_context.hash(pwd)
        account = users(
            user_id=user_id,
            email=email,
            pwd=hashed_pwd,
            status=True,
            permission=False,
            create_time=datetime.now()
        )
        session.add(account)
        session.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 저장됨"})

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()

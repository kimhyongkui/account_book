from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from app.auth import password_hash

Session = sessionmaker(bind=engine)
session = Session()


def create_account(user_id, email, pwd):
    try:
        check_id = session.query(users).filter_by(user_id=user_id).first()
        check_email = session.query(users).filter_by(email=email).first()
        if check_id or check_email:
            result = JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                  content={"message": "이미 존재하는 아이디 또는 이메일입니다."})
        else:
            account = users(
                user_id=user_id,
                email=email,
                pwd=password_hash(pwd),
                status=True,
                permission=False,
                create_time=datetime.now()
            )
            session.add(account)
            session.commit()
            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 저장됨"})
        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()

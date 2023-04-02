from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse
from app.auth import verify_password

Session = sessionmaker(bind=engine)
session = Session()


def delete_user(user_id, email, pwd):
    try:
        search = session.query(users).filter_by(user_id=user_id, email=email, status=True).first()
        if search:
            if verify_password(pwd, search.pwd):
                session.query(users). \
                    filter_by(user_id=user_id, email=email, status=True). \
                    update({"status": False, "permission": False, "create_time": datetime.now()})
                session.commit()
                result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "아이디 삭제 완료"})
            else:
                result = JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "잘못된 비밀번호"})
        else:
            result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "아이디 또는 메일이 잘못됨"})
        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()

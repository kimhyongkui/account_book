from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from app.auth import password_hash

Session = sessionmaker(bind=engine)
session = Session()


def edit_user(user_id, email, pwd):
    try:
        search = session.query(users).filter_by(user_id=user_id, status=True).first()
        if search:
            session.query(users).filter_by(user_id=user_id, status=True). \
                update({"email": email, "pwd": password_hash(pwd), "create_time": datetime.now()})
            session.commit()

            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 수정됨"})
        else:
            result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "데이터를 찾을 수 없습니다"})
        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()

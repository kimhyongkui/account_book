from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def edit_account(user_id, email, pwd):
    result = session.query(users).filter_by(user_id=user_id).first()
    if not result:
        session.close()
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "계정을 찾을 수 없습니다"})
    else:
        session.query(users).filter_by(user_id=user_id). \
            update({"email": email, "pwd": pwd, "create_time": datetime.now()})
        session.commit()
        session.close()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 수정됨"})

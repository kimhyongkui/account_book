from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import account_book
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def edit_account_book(user_id, amount, date, memo):
    result = session.query(account_book).filter_by(user_id=user_id).first()
    if not result:
        session.close()
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "해당 계정의 데이터를 찾을 수 없습니다"})
    else:
        session.query(account_book).filter_by(user_id=user_id). \
            update({"amount": amount, "date": date, "memo": memo, "create_time": datetime.now()})
        session.commit()
        session.close()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 수정됨"})

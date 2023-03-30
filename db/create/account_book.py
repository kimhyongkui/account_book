from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import account_book
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def write_account_book(user_id, amount, date, memo):
    account = account_book(user_id=user_id, amount=amount, date=date, memo=memo, status=True, create_time=datetime.now())
    session.add(account)
    session.commit()
    session.close()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 저장됨"})

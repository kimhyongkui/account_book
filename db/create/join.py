from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def create_account(user_id, email, pwd):
    account = users(user_id=user_id, email=email, pwd=pwd, status=True, create_time=datetime.now())
    session.add(account)
    session.commit()
    session.close()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 저장됨"})
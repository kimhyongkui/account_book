from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import account_book
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()


def edit_account_book(no, user_id, amount, date, memo):
    try:
        search = session.query(account_book).filter_by(no=no, user_id=user_id, status=True).first()
        if not search:
            result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "데이터를 찾을 수 없습니다"})
        else:
            session.query(account_book).filter_by(no=no, user_id=user_id, status=True). \
                update({"amount": amount, "date": date, "memo": memo, "create_time": datetime.now()})
            session.commit()

            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 수정됨"})

        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()

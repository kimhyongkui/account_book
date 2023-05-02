from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Account_book
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()


def edit_account_book(no, user_id, amount, date, memo):
    try:
        search = session.query(Account_book).filter_by(no=no, user_id=user_id, status=True).first()
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

        session.query(Account_book).filter_by(no=no, user_id=user_id, status=True). \
            update({"amount": amount, "date": date, "memo": memo, "create_time": datetime.now()})
        session.commit()

        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 수정 완료."})

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

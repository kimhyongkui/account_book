from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import account_book
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()


def write_account_book(user_id, amount, date, memo):
    try:
        account = account_book(
            user_id=user_id,
            amount=amount,
            date=date,
            memo=memo,
            status=True,
            create_time=datetime.now()
        )
        session.add(account)
        session.commit()

        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "가계부 작성 완료"})

    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

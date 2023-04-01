from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import account_book
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def delete_account_book(user_id, no=None):
    try:
        search = session.query(account_book)
        if no:
            data = search.filter_by(no=no, user_id=user_id, status=True).first()
            if data:
                session.query(account_book).filter_by(no=no, user_id=user_id, status=True). \
                    update({"status": False, "create_time": datetime.now()})
                session.commit()
                result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 삭제됨"})
            else:
                result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "데이터가 없음"})

        else:
            data = search.filter_by(user_id=user_id, status=True).all()
            if data:
                session.query(account_book).filter_by(user_id=user_id, status=True). \
                    update({"status": False, "create_time": datetime.now()})
                session.commit()
                result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "모든 데이터가 삭제됨"})
            else:
                result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "데이터가 없음"})

        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()

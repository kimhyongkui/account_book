from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import account_book
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()


def delete_account_book(user_id, no=None):
    try:
        if no:
            data = session.query(account_book).filter_by(no=no, user_id=user_id, status=True).first()
            if not data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

            session.query(account_book).filter_by(no=no, user_id=user_id, status=True). \
                update({"status": False, "create_time": datetime.now()})
            session.commit()
            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 삭제 완료."})

        else:
            data = session.query(account_book).filter_by(user_id=user_id, status=True).all()
            if not data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

            session.query(account_book).filter_by(user_id=user_id, status=True). \
                update({"status": False, "create_time": datetime.now()})
            session.commit()
            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "모든 데이터가 삭제 완료."})

        return result

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

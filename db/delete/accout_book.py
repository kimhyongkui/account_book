from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import account_book
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def delete_account_book(user_id):
    result = session.query(account_book).filter_by(user_id=user_id).first()
    if not result:
        session.close()
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "계정을 찾을 수 없습니다"})
    else:
        result = session.query(account_book).filter_by(user_id=user_id).all()
        data_list = []
        for data in result:
            data_dict = {
                'user_id': data.user_id,
                'amount': data.amount,
                'date': data.date,
                'memo': data.memo
            }
            data_list.append(data_dict)
        result = data_list
        session.commit()
        session.close()
        return result

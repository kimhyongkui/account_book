from fastapi import status, HTTPException
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Account_book

Session = sessionmaker(bind=engine)
session = Session()


def get_account_book(no, user_id):
    try:
        search = session.query(Account_book).filter_by(no=no, user_id=user_id, status=True).first()
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

        data_dict = {
            'no': search.no,
            'user_id': search.user_id,
            'amount': search.amount,
            'date': search.date,
            'memo': search.memo
        }

        return data_dict

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()


def get_all_account_book(user_id):
    try:
        search = session.query(Account_book).filter_by(user_id=user_id, status=True).all()
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

        data_list = []
        for data in search:
            data_dict = {
                'no': data.no,
                'user_id': data.user_id,
                'amount': data.amount,
                'date': data.date,
                'memo': data.memo
            }
            data_list.append(data_dict)

        return data_list

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

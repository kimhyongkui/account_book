from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users, account_book
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse
from passlib.context import CryptContext

Session = sessionmaker(bind=engine)
session = Session()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def restore_user(user_id, email, pwd):
    try:
        search = session.query(users).filter_by(user_id=user_id, email=email, status=False).first()
        if search:
            if bcrypt_context.verify(pwd, search.pwd):
                session.query(users). \
                    filter_by(user_id=user_id, email=email, status=False). \
                    update({"status": True, "permission": False, "create_time": datetime.now()})
                session.commit()
                result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "아이디 복구 완료"})
            else:
                result = JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "잘못된 비밀번호"})
        else:
            result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "데이터가 없습니다"})

        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()


def restore_account_book(user_id, no=None):
    try:
        search = session.query(account_book)
        if no:
            data = search.filter_by(no=no, user_id=user_id, status=False).first()
            if data:
                session.query(account_book).filter_by(no=no, user_id=user_id, status=False). \
                    update({"status": True, "create_time": datetime.now()})
                session.commit()
                result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 복구 완료"})
            else:
                result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "데이터가 없습니다"})
        else:
            data = search.filter_by(user_id=user_id, status=False).all()
            if data:
                session.query(account_book).filter_by(user_id=user_id, status=False). \
                    update({"status": True, "create_time": datetime.now()})
                session.commit()
                result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "모든 데이터 복구 완료"})
            else:
                result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "데이터가 없습니다"})

        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()

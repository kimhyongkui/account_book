from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from fastapi import status
from fastapi.responses import JSONResponse
from passlib.context import CryptContext

Session = sessionmaker(bind=engine)
session = Session()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def edit_user(user_id, email, pwd):
    try:
        search = session.query(users).filter_by(user_id=user_id, status=True).first()
        if not search:
            result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "계정을 찾을 수 없습니다"})
        else:
            hashed_pwd = bcrypt_context.hash(pwd)
            session.query(users).filter_by(user_id=user_id, status=True). \
                update({"email": email, "pwd": hashed_pwd, "create_time": datetime.now()})
            session.commit()

            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터가 수정됨"})

        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))

    finally:
        session.close()
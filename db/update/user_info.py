from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from app.auth import password_hash

Session = sessionmaker(bind=engine)
session = Session()


def edit_user(user_id, email, pwd):
    try:
        users(email=email, pwd=pwd)
        search = session.query(users).filter_by(user_id=user_id, status=True).first()
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

        session.query(users).filter_by(user_id=user_id, status=True). \
            update({"email": email, "pwd": password_hash(pwd), "create_time": datetime.now()})
        session.commit()

        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 수정 완료."})

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from datetime import datetime
from app.auth import verify_password

Session = sessionmaker(bind=engine)
session = Session()


def delete_user(user_id, email, pwd):
    try:
        search = session.query(users).filter_by(user_id=user_id, email=email, status=True).first()
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="아이디 또는 메일을 확인하세요.")

        if not verify_password(pwd, search.pwd):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="비밀번호가 틀렸습니다.")

        session.query(users). \
            filter_by(user_id=user_id, email=email, status=True). \
            update({"status": False, "create_time": datetime.now()})
        session.commit()

        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "아이디 삭제 완료"})

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

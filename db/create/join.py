from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Users
from datetime import datetime
from app.auth import password_hash

Session = sessionmaker(bind=engine)
session = Session()


def create_account(user_id, email, pwd):
    try:
        check_id = session.query(Users).filter_by(user_id=user_id).first()
        check_email = session.query(Users).filter_by(email=email).first()
        if check_id or check_email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="이미 존재하는 아이디 또는 이메일입니다.")

        account = Users(
            user_id=user_id,
            email=email,
            pwd=password_hash(pwd),
            status=True,
            create_time=datetime.now()
        )
        session.add(account)
        session.commit()

        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "가입 성공."})

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

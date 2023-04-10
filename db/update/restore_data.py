from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users, account_book
from datetime import datetime
from app.auth import verify_password

Session = sessionmaker(bind=engine)
session = Session()


def restore_user(user_id, email, pwd):
    try:
        search = session.query(users).filter_by(user_id=user_id, email=email, status=False).first()
        if not search:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

        if not verify_password(pwd, search.pwd):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="비밀번호가 틀렸습니다.")

        session.query(users). \
            filter_by(user_id=user_id, email=email, status=False). \
            update({"status": True, "create_time": datetime.now()})
        session.commit()

        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "아이디 복구 완료."})

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()


def restore_account_book(user_id, no=None):
    try:
        if no:
            data = session.query(account_book).filter_by(no=no, user_id=user_id, status=False).first()
            if not data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

            session.query(account_book).filter_by(no=no, user_id=user_id, status=False). \
                update({"status": True, "create_time": datetime.now()})
            session.commit()
            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 복구 완료."})

        else:
            data = session.query(account_book).filter_by(user_id=user_id, status=False).all()
            if not data:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터를 찾을 수 없습니다.")

            session.query(account_book).filter_by(user_id=user_id, status=False). \
                update({"status": True, "create_time": datetime.now()})
            session.commit()
            result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "모든 데이터 복구 완료."})

        return result

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

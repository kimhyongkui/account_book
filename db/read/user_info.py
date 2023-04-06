from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def get_user(user_id):
    try:
        result = session.query(users).filter_by(user_id=user_id, status=True).first()
        if not result:
            result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "계정을 찾을 수 없습니다"})

        else:
            result = session.query(users).filter_by(user_id=user_id).first()
            data_dict = {
                'user_id': result.user_id,
                'email': result.email,
                'pwd': result.pwd
            }
            session.commit()
            result = data_dict

        return result

    except Exception as err:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))
    finally:
        session.close()


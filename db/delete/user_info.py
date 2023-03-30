from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def delete_user(user_id):
    result = session.query(users).filter_by(user_id=user_id).first()
    if not result:
        session.close()
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "계정을 찾을 수 없습니다"})
    else:
        result = session.query(users).filter_by(user_id=user_id).first()
        data_dict = {
            'user_id': result.user_id,
            'email': result.email,
            'pwd': result.pwd
        }
        session.commit()
        session.close()
        return data_dict

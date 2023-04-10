from fastapi import status, HTTPException
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users

Session = sessionmaker(bind=engine)
session = Session()


def get_user(user_id):
    try:
        user = session.query(users).filter_by(user_id=user_id, status=True).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="계정을 찾을 수 없습니다.")

        data_dict = {
            'user_id': user.user_id,
            'email': user.email,
            'pwd': user.pwd
        }

        return data_dict

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

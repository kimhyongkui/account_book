from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import users
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from jose import jwt
from app.auth import verify_password


SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

Session = sessionmaker(bind=engine)
session = Session()


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def login(user_id, pwd):
    try:
        user = session.query(users).filter_by(user_id=user_id).first()
        if not user:
            raise HTTPException(status_code=400, detail="아이디가 없거나 틀림")
        if not verify_password(pwd, user.pwd):
            raise HTTPException(status_code=400, detail="비밀번호가 틀림")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.user_id, "permissions": user.permission},
            expires_delta=access_token_expires
        )
        result = {"access_token": access_token, "token_type": "bearer", "user_id": user.user_id}
        return result

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

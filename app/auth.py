from fastapi import Depends, status, HTTPException
from db.models import users
from db.connection import engine
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext

SessionLocal = sessionmaker(bind=engine)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def has_permission(user_id: str, db: Session = Depends(get_db)):
    user = db.query(users).filter_by(user_id=user_id).first()
    if user and user.permission:
        return user_id
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="권한이 없습니다")


def password_hash(pwd):
    return bcrypt_context.hash(pwd)


def verify_password(pwd, hashed_password):
    return bcrypt_context.verify(pwd, hashed_password)


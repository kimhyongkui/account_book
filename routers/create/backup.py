from fastapi import APIRouter
from db.create.login import login_user, logout_user

router = APIRouter()


@router.post('/login', tags=["login"])
def login(user_id, pwd):
    result = login_user(user_id, pwd)
    return result


@router.post('/logout', tags=["logout"])
def logout(user_id):
    result = logout_user(user_id)
    return result

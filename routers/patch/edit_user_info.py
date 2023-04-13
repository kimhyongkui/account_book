from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.update.user_info import edit_user

router = APIRouter()


@router.patch('/user/{user_id}', tags=["update"])
def edit_user_info(email: str, pwd: str, user_id: str = Depends(get_user_auth)):
    result = edit_user(user_id, email, pwd)
    return result

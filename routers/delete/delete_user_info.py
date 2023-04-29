from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.delete.user_info import delete_user

router = APIRouter()


@router.delete('/user', tags=["delete"])
def delete_user_info(email: str, pwd: str, user_id: str = Depends(get_user_auth)):
    result = delete_user(user_id, email, pwd)
    return result

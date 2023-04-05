from fastapi import APIRouter, Depends
from app.auth import get_current_user
from db.delete.user_info import delete_user

router = APIRouter()


@router.delete('/account/{user_id}', tags=["delete"])
def edit_user_info(email, pwd, user_id: str = Depends(get_current_user)):
    result = delete_user(user_id, email, pwd)
    return result

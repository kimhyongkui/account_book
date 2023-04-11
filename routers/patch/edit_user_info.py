from fastapi import APIRouter, Depends
from app.auth import get_current_user
from db.update.user_info import edit_user

router = APIRouter()


@router.patch('/account/{user_id}/update', tags=["update"])
def edit_user_info(email: str, pwd: str, user_id: str = Depends(get_current_user)):
    result = edit_user(user_id, email, pwd)
    return result

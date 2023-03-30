from fastapi import APIRouter
from db.update.user_info import edit_user

router = APIRouter()


@router.put('/account/{user_id}/update', tags=["update"])
def edit_user_info(user_id, email, pwd):
    result = edit_user(user_id, email, pwd)
    return result

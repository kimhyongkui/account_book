from fastapi import APIRouter, Depends
from app.auth import has_permission
from db.update.user_info import edit_user

router = APIRouter()


@router.put('/account/{user_id}/update', tags=["update"])
def edit_user_info(email, pwd, user_id: str = Depends(has_permission)):
    result = edit_user(user_id, email, pwd)
    return result

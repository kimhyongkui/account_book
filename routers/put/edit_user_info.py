from fastapi import APIRouter
from db.update.user_info import edit_user

router = APIRouter()


@router.put('/account/{user_id}', tags=["update"])
def edit_user_info(user_id, pwd, email):
    result = edit_user(user_id, pwd, email)
    return result

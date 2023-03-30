from fastapi import APIRouter
from db.delede.user_info import delete_user

router = APIRouter()


@router.put('/account/{user_id}', tags=["delete"])
def edit_user_info(user_id, pwd, email):
    result = delete_user(user_id, pwd, email)
    return result

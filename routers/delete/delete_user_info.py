from fastapi import APIRouter
from db.delete.user_info import delete_user

router = APIRouter()


@router.delete('/account/{user_id}', tags=["delete"])
def edit_user_info(user_id, email, pwd):
    result = delete_user(user_id, email, pwd)
    return result

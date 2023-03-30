from fastapi import APIRouter
from db.read.user_info import get_user

router = APIRouter()


@router.get('/account/{user_id}', tags=["get"])
def get_user_info(user_id):
    result = get_user(user_id)
    return result

from fastapi import APIRouter, Depends
from app.auth import has_permission
from db.read.user_info import get_user

router = APIRouter()


@router.get('/user/{user_id}', tags=["get"])
def get_user_info(user_id: str = Depends(has_permission)):
    result = get_user(user_id)
    return result

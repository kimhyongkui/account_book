from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.read.user_info import get_user

router = APIRouter()


@router.get("/info/user", tags=["get"])
def get_current_user_info(user_id: str = Depends(get_user_auth)):
    user = get_user(user_id)
    return user

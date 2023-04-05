from fastapi import APIRouter, Depends
from db.read.user_info import get_user
from app.auth import get_current_user

router = APIRouter(prefix="/user")


@router.get("/user/user-id", tags=["user"])
async def get_current_user_info(user_id: str = Depends(get_current_user)):
    user = get_user(user_id)
    return user

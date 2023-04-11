from fastapi import APIRouter, Depends
from app.auth import get_current_user
from db.read.user_info import get_user

router = APIRouter()


@router.get("/account/{user_id}", tags=["get"])
async def get_current_user_info(user_id: str = Depends(get_current_user)):
    user = get_user(user_id)
    return user

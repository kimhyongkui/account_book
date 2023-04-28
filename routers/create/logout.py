from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.create.logout import delete_token

router = APIRouter()


@router.post("/logout", tags=["logout"])
def logout_jwt(user_id: str = Depends(get_user_auth)):
    result = delete_token(user_id)
    return result

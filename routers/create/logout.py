from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.create import logout

router = APIRouter()


@router.post("/logout", tags=["logout"])
def logout_jwt(user_id: str = Depends(get_user_auth)):
    result = logout(user_id)
    return result

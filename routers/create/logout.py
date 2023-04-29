from fastapi import APIRouter, Depends
from app.auth import oauth2_scheme
from db.create.logout import logout_jwt

router = APIRouter()


@router.post("/logout", tags=["logout"])
def logout(token: str = Depends(oauth2_scheme)):
    result = logout_jwt(token)
    return result

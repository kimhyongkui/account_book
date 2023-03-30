# from fastapi import APIRouter
# from db.read.user_info import get_user
#
# router = APIRouter()
#
#
# @router.get('/account/{user_id}', tags=["get"])
# def get_user_info(user_id):
#     result = get_user(user_id)
#     return result
from fastapi import APIRouter, Depends, HTTPException

from db.create.login import decode_token
from db.read.user_info import get_user
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/account-book/login")


@router.get('/account/{user_id}', tags=["get"])
def get_user_info(user_id, token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload or payload["sub"] != user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    result = get_user(user_id)
    if not result:
        raise HTTPException

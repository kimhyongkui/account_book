from fastapi import APIRouter
from db.create.join import create_account

router = APIRouter()


@router.post('/join', tags=["create"])
def join(user_id: str, email: str, pwd: str):
    result = create_account(user_id, email, pwd)
    return result

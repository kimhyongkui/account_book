from fastapi import APIRouter
from db.create.join import create_account

router = APIRouter(prefix="/join")


@router.post('/join', tags=["create"])
def join(user_id, email, pwd):
    result = create_account(user_id, email, pwd)
    return result
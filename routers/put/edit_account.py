from fastapi import APIRouter
from db.update.edit_account import edit_account

router = APIRouter(prefix="/account")


@router.post('/account/{user_id}')
def edit_account_info(user_id, pwd, email):
    result = edit_account(user_id, pwd, email)
    return result

from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.create.account_book import write_account_book

router = APIRouter()


@router.post('/account-book', tags=["create"])
def create_account_book(amount: int, date: str, memo: str, user_id: str = Depends(get_user_auth)):
    result = write_account_book(user_id, amount, date, memo)
    return result

from fastapi import APIRouter, Depends
from app.auth import get_current_user
from db.create.account_book import write_account_book

router = APIRouter()


@router.post('/account-book', tags=["create"])
def write_account_book_info(amount: int, date: str, memo: str, user_id: str = Depends(get_current_user)):
    result = write_account_book(user_id, amount, date, memo)
    return result

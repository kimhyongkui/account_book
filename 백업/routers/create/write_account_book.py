from fastapi import APIRouter, Depends
from app.auth import has_permission
from db.create.account_book import write_account_book

router = APIRouter()


@router.post('/account-book', tags=["create"])
def write_account_book_info(amount, date, memo, user_id: str = Depends(has_permission)):
    result = write_account_book(user_id, amount, date, memo)
    return result

from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.update.account_book import edit_account_book

router = APIRouter()


@router.patch('/book/{user_id}', tags=["update"])
def edit_account_book_info(no: int, amount: int, date: str, memo: str, user_id: str = Depends(get_user_auth)):
    result = edit_account_book(no, user_id, amount, date, memo)
    return result

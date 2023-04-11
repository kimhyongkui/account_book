from fastapi import APIRouter, Depends
from app.auth import get_current_user
from db.update.account_book import edit_account_book

router = APIRouter()


@router.patch('/account-book/{user_id}/update', tags=["update"])
def edit_account_book_info(no: int, amount: int, date: str, memo: str, user_id: str = Depends(get_current_user)):
    result = edit_account_book(no, user_id, amount, date, memo)
    return result

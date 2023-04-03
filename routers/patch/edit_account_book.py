from fastapi import APIRouter, Depends
from db.update.account_book import edit_account_book
from app.auth import has_permission

router = APIRouter()


@router.patch('/account-book/{user_id}/update', tags=["update"])
def edit_account_book_info(no, amount, date, memo, user_id: str = Depends(has_permission)):
    result = edit_account_book(no, user_id, amount, date, memo)
    return result

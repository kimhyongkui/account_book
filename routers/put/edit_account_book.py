from fastapi import APIRouter
from db.update.account_book import edit_account_book

router = APIRouter()


@router.put('/account-book/{user_id}/update', tags=["update"])
def edit_account_book_info(no, user_id, amount, date, memo):
    result = edit_account_book(no, user_id, amount, date, memo)
    return result

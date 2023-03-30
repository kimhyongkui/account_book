from fastapi import APIRouter
from db.update.account_book import edit_account_book

router = APIRouter()


@router.put('/account-book/{user_id}', tags=["update"])
def edit_account_book_info(user_id, amount, date, memo):
    result = edit_account_book(user_id, amount, date, memo)
    return result

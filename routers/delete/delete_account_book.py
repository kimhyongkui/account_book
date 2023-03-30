from fastapi import APIRouter
from db.delete.account_book import delete_account_book

router = APIRouter()


@router.put('/account-book/{user_id}', tags=["delete"])
def edit_account_book_info(user_id, amount, date, memo):
    result = delete_account_book(user_id, amount, date, memo)
    return result

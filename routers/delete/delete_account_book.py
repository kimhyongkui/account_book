from fastapi import APIRouter
from db.delete.account_book import delete_account_book

router = APIRouter(prefix="/account-book")


@router.delete('/specific/{user_id}', tags=["delete"])
def delete_account_book_info(user_id, no):
    result = delete_account_book(user_id, no)
    return result


@router.delete('/all/{user_id}', tags=["delete"])
def delete_all_account_book_info(user_id):
    result = delete_account_book(user_id)
    return result

from fastapi import APIRouter
from db.read.account_book import get_account_book

router = APIRouter()


@router.get('/account-book/{user_id}', tags=["get"])
def get_account_book_info(user_id):
    result = get_account_book(user_id)
    return result

from fastapi import APIRouter
from db.create.account_book import write_account_book

router = APIRouter()


@router.post('/account-book/{user_id}', tags=["create"])
def write_account_book_info(user_id, amount, date, memo):
    result = write_account_book(user_id, amount, date, memo)
    return result

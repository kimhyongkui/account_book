from fastapi import APIRouter, Depends
from app.auth import has_permission
from db.read.account_book import get_account_book, get_all_account_book

router = APIRouter()


@router.get('/account-book/{user_id}/no', tags=["get"])
def get_all_account_book_info(no, user_id: str = Depends(has_permission)):
    result = get_account_book(no, user_id)
    return result


@router.get('/account-book/{user_id}/all', tags=["get"])
def get_specific_account_book_info(user_id: str = Depends(has_permission)):
    result = get_all_account_book(user_id)
    return result

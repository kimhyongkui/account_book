from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.read.account_book import get_account_book, get_all_account_book

router = APIRouter(prefix="/info")


@router.get('/book/no', tags=["get"])
def get_specific_account_book_info(no: int, user_id: str = Depends(get_user_auth)):
    result = get_account_book(no, user_id)
    return result


@router.get('/book/all', tags=["get"])
def get_all_account_book_info(user_id: str = Depends(get_user_auth)):
    result = get_all_account_book(user_id)
    return result

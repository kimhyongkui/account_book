from fastapi import APIRouter, Depends
from app.auth import get_current_user
from db.delete.account_book import delete_account_book

router = APIRouter(prefix="/account-book")


@router.delete('/specific/{user_id}', tags=["delete"])
def delete_account_book_info(no: int, user_id: str = Depends(get_current_user)):
    result = delete_account_book(user_id, no)
    return result


@router.delete('/all/{user_id}', tags=["delete"])
def delete_all_account_book_info(user_id: str = Depends(get_current_user)):
    result = delete_account_book(user_id)
    return result

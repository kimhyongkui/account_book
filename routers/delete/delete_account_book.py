from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.delete.account_book import delete_account_book

router = APIRouter()


@router.delete('/book/{user_id}/no', tags=["delete"])
def delete_account_book_info(no: int, user_id: str = Depends(get_user_auth)):
    result = delete_account_book(user_id, no)
    return result


@router.delete('/book/{user_id}/all', tags=["delete"])
def delete_all_account_book_info(user_id: str = Depends(get_user_auth)):
    result = delete_account_book(user_id)
    return result

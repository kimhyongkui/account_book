from fastapi import APIRouter, Depends
from app.auth import get_user_auth
from db.update.restore_data import restore_user, restore_account_book

router = APIRouter(prefix="/restore")


@router.patch('/user', tags=["restore"])
def restore_user_info(user_id: str, email: str, pwd: str):
    result = restore_user(user_id, email, pwd)
    return result


@router.patch('/book/no', tags=["restore"])
def restore_account_book_info(no: int, user_id: str = Depends(get_user_auth)):
    result = restore_account_book(user_id, no)
    return result


@router.patch('/book/all', tags=["restore"])
def restore_all_account_book_info(user_id: str = Depends(get_user_auth)):
    result = restore_account_book(user_id)
    return result

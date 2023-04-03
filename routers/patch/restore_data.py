from fastapi import APIRouter, Depends
from app.auth import has_permission
from db.update.restore_data import restore_user, restore_account_book

router = APIRouter()


@router.patch('/account/{user_id}/restore', tags=["restore"])
def restore_user_info(user_id, email, pwd):
    result = restore_user(user_id, email, pwd)
    return result


@router.patch('/account-book/{user_id}/restore', tags=["restore"])
def restore_account_book_info(no, user_id: str = Depends(has_permission)):
    result = restore_account_book(user_id, no)
    return result


@router.patch('/account-book/{user_id}/restore-all', tags=["restore"])
def restore_all_account_book_info(user_id: str = Depends(has_permission)):
    result = restore_account_book(user_id)
    return result

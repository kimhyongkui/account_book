from fastapi import APIRouter
from db.update.restore_data import restore_user, restore_account_book

router = APIRouter()


@router.put('/account/{user_id}/restore', tags=["restore"])
def restore_user_info(user_id, email, pwd):
    result = restore_user(user_id, email, pwd)
    return result


@router.put('/account-book/{user_id}/restore', tags=["restore"])
def restore_account_book_info(user_id, no):
    result = restore_account_book(user_id, no)
    return result


@router.put('/account-book/{user_id}/restore-all', tags=["restore"])
def restore_all_account_book_info(user_id):
    result = restore_account_book(user_id)
    return result

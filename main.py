from fastapi import FastAPI
from routers.create import join, write_account_book, login
from routers.read import get_user_info, get_account_book
from routers.put import edit_user_info, edit_account_book, restore_data
from routers.delete import delete_user_info, delete_account_book
import uvicorn

app = FastAPI(title="account_book")

app.include_router(join.router, prefix="/account-book")
app.include_router(login.router, prefix="/account-book")
app.include_router(write_account_book.router, prefix="/account-book")

app.include_router(get_user_info.router, prefix="/account-book")
app.include_router(get_account_book.router, prefix="/account-book")

app.include_router(edit_user_info.router, prefix="/account-book")
app.include_router(edit_account_book.router, prefix="/account-book")
app.include_router(restore_data.router, prefix="/account-book")

app.include_router(delete_user_info.router, prefix="/account-book")
app.include_router(delete_account_book.router, prefix="/account-book")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8080
    )

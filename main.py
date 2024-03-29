from fastapi import FastAPI
from routers.create import join, create_account_book, login, logout
from routers.read import get_user_info, get_account_book
from routers.patch import edit_user_info, edit_account_book, restore_data
from routers.delete import delete_user_info, delete_account_book
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="account_book")

app.include_router(join.router, prefix="/account-book")
app.include_router(login.router, prefix="/account-book")
app.include_router(logout.router, prefix="/account-book")
app.include_router(create_account_book.router, prefix="/account-book")

app.include_router(get_user_info.router, prefix="/account-book")
app.include_router(get_account_book.router, prefix="/account-book")

app.include_router(edit_user_info.router, prefix="/account-book")
app.include_router(edit_account_book.router, prefix="/account-book")
app.include_router(restore_data.router, prefix="/account-book")

app.include_router(delete_user_info.router, prefix="/account-book")
app.include_router(delete_account_book.router, prefix="/account-book")


def main():
    environment = os.getenv("ENVIRONMENT")
    if environment == "local":
        host = "localhost"
        port = 8050
    else:
        host = os.getenv("SERVER_HOST")
        port = int(os.getenv("SERVER_PORT"))

    uvicorn.run("main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    main()

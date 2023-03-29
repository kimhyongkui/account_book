from fastapi import FastAPI
from routers.post import join
from routers.put import edit_account
import uvicorn

app = FastAPI(title="account_book")

app.include_router(join.router, prefix="/account-book")
app.include_router(edit_account.router, prefix="/account-book")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8080
    )

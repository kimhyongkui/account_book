from fastapi import FastAPI
import uvicorn

app = FastAPI(title="account_book")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8080
    )

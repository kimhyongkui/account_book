from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
# from datetime import datetime
# from typing import List

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/account-book/login")

blacklist = set()

def delete_token(token: str = Depends(oauth2_scheme)):
    if token in blacklist:
        raise HTTPException(status_code=400, detail="이미 토큰이 취소되었습니다")
    blacklist.add(token)
    return {"message": "로그아웃 되었습니다."}



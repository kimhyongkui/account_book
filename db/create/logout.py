from fastapi import HTTPException

blacklist = set()


def logout_jwt(token):
    if token in blacklist:
        raise HTTPException(status_code=400, detail="이미 토큰이 취소되었습니다")
    blacklist.add(token)
    return {"message": "로그아웃 되었습니다."}

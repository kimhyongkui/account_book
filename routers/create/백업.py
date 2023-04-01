from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db.create.login import login_user, logout_user

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post('/login', tags=["login"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_id = form_data.username
    pwd = form_data.password
    result = login_user(user_id, pwd)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": result}


@router.post('/logout', tags=["logout"])
def logout(token: str = Depends(oauth2_scheme)):
    user_id = token["sub"]
    result = logout_user(user_id)
    if not result:
        raise HTTPException(status_code=400, detail="Failed to logout")
    return {"detail": "Successfully logged out"}


# def delete_user(user_id, email, pwd):
#     try:
#         search = session.query(users).filter_by(user_id=user_id, email=email, status=True).first()
#         if not search:
#             result = JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "아이디가 없음"})
#         else:
#             hashed_pwd = bcrypt_context.hash(pwd)
#             session.query(users). \
#                 filter_by(user_id=user_id, email=email, status=True). \
#                 update({"status": False, "create_time": datetime.now()})
#             session.commit()
#             result = JSONResponse(status_code=status.HTTP_200_OK, content={"message": "아이디 삭제 완료"})
#
#         return result
#
#     except Exception as err:
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(err))
#
#     finally:
#         session.close()
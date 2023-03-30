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

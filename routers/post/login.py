from fastapi import APIRouter
from db.create.login import

router = APIRouter(prefix="/join")


@router.post('/join')
def join():

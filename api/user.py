from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union

from dependencies.get_db import get_db
from db import sql
from serializers import users
from services import crud_user

router = APIRouter()

@router.get("/main")
async def main(name: str):
    return{
        "msg": f"Hello, {name}!"
    }


@router.post("/create_user")
async def create_user(new_user: users.NewUserRequest, db: Session = Depends(get_db)):
    """_summary_

    __Args__:
        new_user (users.NewUserRequest): Данные пользователя при запросе на регистрацию

    __Returns__:
        _dict_ : Индикатор успеха исполнения регистрации
    """
    if "@" in new_user.email and len(new_user.email.split('.')[-1])>=2:
        return await crud_user.create_user(db, new_user)
    return {
        "success": False,
        "message": "Incorrect email"
    }

# TODO
# login
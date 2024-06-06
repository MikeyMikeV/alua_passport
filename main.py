import uvicorn
from fastapi import FastAPI
from typing import Union

import serializers as sr
from config import get_settings

app = FastAPI(title=get_settings().title)


@app.get("/main")
async def main(name: str):
    return{
        "msg": f"Hello, {name}!"
    }


@app.post("/create_user", response_model=Union[sr.NewUserErrorResponse, sr.NewUserSuccessResponse])
async def create_user(new_user: sr.NewUserRequest):
    """_summary_

    __Args__:
        new_user (sr.NewUserRequest): Данные пользователя при запросе на регистрацию

    __Returns__:
        _dict_ : Индикатор успеха исполнения регистрации
    """
    if "@" in new_user.email and len(new_user.email.split('.')[-1])>=2:
        return {
            "success": True
        }
    return {
        "success": False,
        "message": "Incorrect email"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=get_settings().port,
        host=get_settings().host,
        reload=get_settings().reload,
        log_level=get_settings().log_level
    )
from pydantic import BaseModel, Field


class NewUserRequest(BaseModel):
    """_summary_

    Данные пользователя при запросе на регистрацию
    """
    email: str = Field(description="Эл. почта нового пользователя", examples=["example@mail.ex"])
    password: str = Field(description="Пароль нового пользователя", examples=["@goodPassword12345678"])
    name: str = Field(description="Имя нового пользователя" , default=None, examples=["Name"])
    lastname: str = Field(description="Фамилия нового пользователя" , default=None, examples=["Lastname"])


class NewUserSuccessResponse(BaseModel):
    success: bool


class NewUserErrorResponse(BaseModel):
    success: bool
    message: str
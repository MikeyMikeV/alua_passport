import uvicorn
from fastapi import FastAPI
from config import get_settings

from api import user, google_auth

app = FastAPI(title=get_settings().title)
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(google_auth.router, prefix="/google", tags=["Google Auth"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=get_settings().port,
        host=get_settings().host,
        reload=False,
        log_level=get_settings().log_level
    )
import os
from dotenv import load_dotenv
from functools import  lru_cache


class Settings:
    title = "Passport-FastAPI"
    def __init__(self) -> None:
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self.POSTGRES_URL = os.getenv("POSTGRES_URL")
        self.node_env = os.getenv("NODE_ENV")
        self.reload=True if self.node_env == "development" else False
        self.log_level="debug" if self.node_env == "development" else "critical"
        self.host = "localhost" if self.node_env == "development" else "0.0.0.0"
        self.port = 21015

@lru_cache
def get_settings():
    return Settings()
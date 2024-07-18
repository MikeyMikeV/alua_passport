from fastapi import APIRouter
from typing import Union

from serializers import users

router = APIRouter()

@router.get("/")
async def main():
    return "Hello"
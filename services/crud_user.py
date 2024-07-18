from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime

from serializers import users


async def create_user(db: Session, data: users.NewUserRequest):
    db_data = db.execute(text(f"""
INSERT INTO 
    users (email, password, username, name, lastname, created_at)
VALUES 
    ('{data.email}', '{data.password}', '{data.username}', '{data.name}', '{data.lastname}', '{datetime.now()}');
"""))
    db.commit()
    print(db_data)
    return {"success": True}
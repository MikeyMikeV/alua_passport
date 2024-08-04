from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime

from serializers import users


async def create_user(db: Session, data: users.NewUserRequest):
    db_user = db.execute(text(f"""
        SELECT id, email from users
        WHERE email = '{data.email}'                         
    """)).mappings().all()
    
    if len(db_user)>0:
        return {
            "success": False,
            "message": "Пользователь с таким email уже существует"
        }

    db_data = db.execute(text(f"""
INSERT INTO 
    users (email, password, username, name, lastname, created_at)
VALUES 
    ('{data.email}', '{data.password}', '{data.username}', '{data.name}', '{data.lastname}', '{datetime.now()}');
"""))
    db.commit()
    return {"success": True}
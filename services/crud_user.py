import base64
from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime
from hashlib import pbkdf2_hmac
from random import randbytes

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


    salt = base64.b64encode(randbytes(32)).decode()
    hash_res = pbkdf2_hmac(
        "sha512", data.password.encode(), base64.b64decode(salt.encode()), 11223, 32
    )
    hash_res = base64.b64encode(hash_res).decode()
    
    db_data = db.execute(text(f"""
INSERT INTO 
    users (email, password, username, name, lastname, created_at, salt)
VALUES 
    ('{data.email}', '{hash_res}', '{data.username}', '{data.name}', '{data.lastname}', '{datetime.now()}', '{salt}');
"""))   
    db.commit()
    return {"success": True}
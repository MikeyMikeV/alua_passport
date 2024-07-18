from db.sql import SessionLocal


# Функция для открытия сессии для единичного запроса через ORM
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

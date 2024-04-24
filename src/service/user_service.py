from src.schemas.user_schema import UserSchema
from src.database.crud import user_crud
from src.database.db import get_db

class UserService():
    def __init__(self):
        self.db = get_db()

    def create_user(self, user: UserSchema):
        try:
            db_user = user_crud.create_user(self.db, user=user)
        except Exception as e:
            raise e
        
        return db_user.id_user
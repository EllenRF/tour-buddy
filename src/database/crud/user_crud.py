from sqlalchemy.orm import Session
from src.models.user_model import UserModel, Base
from src.schemas.user_schema import UserSchema
from uuid import UUID, uuid4

def get_user(db: Session, user_id: UUID):
    return db.query(UserModel).filter(UserModel.id_user == user_id).first()

def create_user(db: Session, user: UserSchema):
    fake_hashed = user.password + "fakehash"
    id_user = uuid4()
    db_user = UserModel(
        id_user=id_user,
        name=user.name,
        email=user.email,
        password=fake_hashed,
        phone_number=user.phone_number,
        data_birth=user.data_birth,
        cpf=user.cpf,
        user_type=user.user_type,
        id_avatar_url=user.id_avatar_url
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

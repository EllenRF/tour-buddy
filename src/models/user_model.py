from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from src.enum import UserType
from src.database.db import engine
from src.database import Base

class UserModel(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone_number = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    data_birth = Column(Date)
    id_avatar_url = Column(String, nullable=True)
    cpf = Column(String)
    user_type = Column(Enum(UserType))
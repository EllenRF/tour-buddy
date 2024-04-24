from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from src.schemas.address_schema import AddressSchema
from src.enum import UserType

class UserSchema(BaseModel):
    user_id: UUID
    name: str
    password: str
    email: str
    phone_number: str
    address: AddressSchema
    date_birth: datetime
    cpf: str
    user_type: UserType
    id_avatar_url: str | None = None

    class Config:
        orm_mode = True
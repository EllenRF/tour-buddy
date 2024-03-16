from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from src.schemas.address_schema import AddressSchema
from src.enum import UserType

class UserSchema(BaseModel):
    user_id: UUID
    name: str
    email: str
    phone_number: str
    address: AddressSchema
    date_birth: datetime
    avatar_url: str
    cpf: str
    user_type: UserType
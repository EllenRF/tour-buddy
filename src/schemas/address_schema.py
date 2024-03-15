from pydantic import BaseModel
from uuid import UUID
from src.schemas import CitySchema, StateSchema

class AddressSchema(BaseModel):
    address_id: UUID
    state: StateSchem
    city: CitySchema
    cep: str
    street: str
    neighborhood: str
    complement: str
from pydantic import BaseModel
from uuid import UUID
from src.schemas.state_schema import StateSchema
from src.schemas.city_schema import CitySchema

class AddressSchema(BaseModel):
    address_id: UUID
    state: StateSchema
    city: CitySchema
    cep: str
    street: str
    neighborhood: str
    complement: str
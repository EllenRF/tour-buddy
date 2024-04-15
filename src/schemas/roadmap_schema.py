from pydantic import BaseModel
from typing import List
from uuid import UUID
from src.schemas.address_schema import AddressSchema

class RoadmapSchema(BaseModel):
    roadmap_id: UUID
    user_id: UUID
    title: str
    description: str
    price: float
    places: List[AddressSchema]
    images: List[str] | None = None

    class Config:
        orm_mode = True
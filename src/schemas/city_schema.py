from pydantic import BaseModel

class CitySchema(BaseModel):
    city_id: int
    name: str
    state_id: int
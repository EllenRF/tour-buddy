from pydantic import BaseModel


class StateSchema(BaseModel):
    state_id: int
    name: str
    acronym: str
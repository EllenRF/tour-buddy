from pydantic import BaseModel


class SignUpSchema(BaseModel):
    email: str
    password: str

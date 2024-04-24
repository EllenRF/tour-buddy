from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request

import firebase_admin
from firebase_admin import credentials, auth
from src.schemas import UserSchema
from src.utils import firebase_config, firebase_certificate_credentials
from src.service import UserService
import pyrebase

router = APIRouter(prefix="/user")


if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_certificate_credentials)
    firebase_admin.initialize_app(cred)



firebase = pyrebase.initialize_app(firebase_config)


@router.post("/")
async def create_user(user: UserSchema, response_model=UserSchema):
    try:
        user = UserService()
        created_user = user.create_user(user=UserSchema)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error: {e}",
        )

    return JSONResponse(content={"data": user}, status_code=201)

@router.delete("/")
async def delete_user():
    pass
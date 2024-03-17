from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request

import firebase_admin
from firebase_admin import credentials, auth
from src.schemas import LoginSchema, SignUpSchema
from src.utils import firebase_config
import pyrebase

router = APIRouter(prefix="/user")


if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)



firebase = pyrebase.initialize_app(firebase_config)


@router.post("/")
async def create_user(user: User):
    try:
        user = user.service_create_user()
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error: {e}",
        )

    return JSONResponse(content={"data": user}, status_code=201)

@router.delete("/")
async def delete_user():
    pass
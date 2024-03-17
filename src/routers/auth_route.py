from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from firebase_admin import credentials, auth
from src.schemas import LoginSchema, SignUpSchema
from src.utils import firebase_config, firebase_certificate_credentials
import pyrebase
import firebase_admin

router = APIRouter(prefix="/auth")


if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_certificate_credentials)
    firebase_admin.initialize_app(cred)



firebase = pyrebase.initialize_app(firebase_config)


@router.post("/signup")
async def create_account(user_data: SignUpSchema):
    try:
        user = auth.create_user(email=user_data.email, password=user_data.password)
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail=f"Account already created for the email: {user_data.email}",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {e}")

    return JSONResponse(content={"user_id": user.uid}, status_code=201)


@router.post("/login")
async def create_access_token(user_data: LoginSchema):
    try:
        user = firebase.auth().sign_in_with_email_and_password(
            email=user_data.email, password=user_data.password
        )

        token = user["idToken"]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid Credentials")

    return JSONResponse(content={"token": token}, status_code=200)


@router.post("/validate-token")
async def validate_token(requests: Request):
    headers = requests.headers
    jwt = headers.get("authorization")

    user = auth.verify_id_token(jwt)

    return user["user_id"]

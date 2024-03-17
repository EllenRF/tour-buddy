from fastapi import FastAPI
from src.routers import auth_route, user_route
import uvicorn


app = FastAPI(title="Backend TCC")
app.include_router(auth_route.router, tags=["auth"])
app.include_router(user_route.router, tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

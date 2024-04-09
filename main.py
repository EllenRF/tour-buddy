from fastapi import FastAPI
import uvicorn
from src.routers import auth_route, user_route
from src.database.db import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend TCC")
app.include_router(auth_route.router, tags=["auth"])
app.include_router(user_route.router, tags=["users"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

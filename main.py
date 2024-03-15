from fastapi import FastAPI
from src.routers import auth
import uvicorn
import os


app = FastAPI(title="Backend TCC")
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

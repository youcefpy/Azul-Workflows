from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router

from backend.database import SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

async def get_db():
    
    async with SessionLocal() as session:
        yield session

app.include_router(router)
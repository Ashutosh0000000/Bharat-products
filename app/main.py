from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db import engine
from app.api import products

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/api")
def root():
    return {"message": "Welcome to Bharat Product Intelligence API"}

app.include_router(products.router)

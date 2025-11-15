import os

from fastapi import FastAPI
from sqlmodel import SQLModel, Field, Session, create_engine, Relationship, text

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + Postgresql running!"}

@app.get("/test-db")
def test_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"db_result": result.one()[0]}

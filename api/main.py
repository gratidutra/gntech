from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = "postgresql+psycopg2://meuusuario:minhasenha@postgres:5432/meubanco"

engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/")
def read_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM repositories"))  
        data = [dict(row) for row in result.mappings()]
    return {"dados": data}

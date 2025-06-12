from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Repositorio(Base):
    __tablename__ = 'repositorios'

    repository_name = Column(String, primary_key=True)
    language = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

def cria_tabelas():
    Base.metadata.create_all(bind=engine)

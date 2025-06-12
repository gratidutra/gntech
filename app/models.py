import os

from dotenv import load_dotenv
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Repository(Base):
    __tablename__ = "repositories"

    repository_name = Column(String, primary_key=True)
    language = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


def create_table():
    Base.metadata.create_all(bind=engine)

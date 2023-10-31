from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

db_url=f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_URL}/{settings.DB_NAME}"

engine=create_engine(db_url)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
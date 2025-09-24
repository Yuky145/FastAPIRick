from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Reemplaza con tus credenciales de RDS
DB_USER = "postgres"
DB_PASSWORD = "uide.123"
DB_HOST = "fastapi-db.c762asqgy46c.us-east-2.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "fastapi-db"  # o el nombre que le pusiste a la BD

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia para usar en tus endpoints de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

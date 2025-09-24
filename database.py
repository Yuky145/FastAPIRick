from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "fastapi-db.c762asqgy46c.us-east-2.rds.amazonaws.com"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)

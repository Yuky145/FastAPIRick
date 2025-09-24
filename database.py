from sqlmodel import SQLModel, create_engine, Session

DB_USER = "postgres"
DB_PASSWORD = "uide.123"
DB_HOST = "fastapi-db.c762asqgy46c.us-east-2.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "fastapi-db"  # o el nombre que le pusiste a la BD

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crea el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Función para inicializar la base de datos (crear tablas)
def init_db():
    SQLModel.metadata.create_all(engine)

# Función para obtener sesión en los endpoints
def get_session():
    with Session(engine) as session:
        yield session

from fastapi import FastAPI
from database import create_db_and_tables
from routers.tasks import router as tasks_router

app = FastAPI(title="ToDo API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(tasks_router)

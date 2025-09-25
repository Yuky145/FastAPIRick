from fastapi import FastAPI, Depends
from sqlmodel import Session
from database import get_session, init_db
from models import Usuario, Libro
import crud

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

# ✅ Cambié get_db por get_session para usar la función correcta
@app.get("/test-db")
def test_db(session: Session = Depends(get_session)):
    return {"status": "Conexión a RDS exitosa!"}

# Endpoints Usuarios
@app.post("/usuarios/")
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    return crud.crear_usuario(session, usuario)

@app.get("/usuarios/")
def listar_usuarios(session: Session = Depends(get_session)):
    return crud.obtener_usuarios(session)

# Endpoints Libros
@app.post("/libros/")
def crear_libro(libro: Libro, session: Session = Depends(get_session)):
    return crud.crear_libro(session, libro)

@app.get("/libros/")
def listar_libros(session: Session = Depends(get_session)):
    return crud.obtener_libros(session)

from sqlmodel import Session, select
from models import Usuario, Libro

# CRUD para Usuarios
def crear_usuario(session: Session, usuario: Usuario):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

def obtener_usuarios(session: Session):
    return session.exec(select(Usuario)).all()

# CRUD para Libros
def crear_libro(session: Session, libro: Libro):
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

def obtener_libros(session: Session):
    return session.exec(select(Libro)).all()

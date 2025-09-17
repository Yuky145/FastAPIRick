from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str

    libros: list["Libro"] = Relationship(back_populates="usuario")

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str
    usuario_id: Optional[int] = Field(default=None, foreign_key="usuario.id")

    usuario: Optional[Usuario] = Relationship(back_populates="libros")

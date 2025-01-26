'''Modelos de datos para la aplicacion CRUD'''

from typing import List,Optional
from uuid import UUID,uuid4
'''Crea llaves primarias'''
from pydantic import BaseModel
from enum import Enum

class Genero(str, Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class Role(str,Enum):
    admin = "admin"
    user = "user"
class Usuario(BaseModel):
    id: Optional[UUID] = uuid4()
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
class UpdateUsuario(BaseModel):
    nombre:Optional[str]
    apellidos: Optional[str]
    genero: Optional[Genero]
    roles: Optional[List[Role]]


from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
'''Importando los modelos'''
from models import Usuario,Genero, Role, UpdateUsuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre= "Marco Antonioo",
        apellidos="Santos Quiros",
        genero=Genero.Masculino,
        roles=[Role.admin],
        ),
        Usuario(
        id=uuid4(),
        nombre= "Amauri",
        apellidos="Santos Quiros",
        genero=Genero.Masculino,
        roles=[Role.user],
    ),
        Usuario(
        id=uuid4(),
        nombre= "Hector",
        apellidos="Santos Quiros",
        genero=Genero.Masculino,
        roles=[Role.user],
    )  
]

@app.get("/")
async def root():
    '''Bienvenida'''
    return("Bienvenido","Hola simples mortales de js")

@app.get("/suma")
async def calcular_edad(anio_nacimiento: int, anio_actual: int):
    '''Calcular edad'''
    edad: int =  anio_actual  - anio_nacimiento
    return edad
print("Tu edad es:",calcular_edad(2002, 2025))


@app.get("/api/usuarios")
async def get_usuarios():
    return db

@app.post("/api/usuarios")
async def inser_usuarios(usuario: Usuario):
    db.append(usuario)
    return {id:usuario.id}

@app.delete("/api/eliminar/{id}")
async def delete_usuarios(id:UUID):
    for usuario in db:
        if usuario.id == id:
            db.remove(usuario)
            return
        raise HTTPException(status_code=404, detail=f"Error al eliminar, id {id} falla.") 
    

@app.put("/api/usuarios/{id}")
async def update_usuarios(user_update: UpdateUsuario, id:UUID):
    for usuario in db:
        if usuario.id == id:
            if user_update.nombre is not None:
                usuario.name = user_update.nombre
            if user_update.apellidos is not None:
                usuario.name = user_update.apellidos
            if user_update.genero is not None:
                usuario.name = user_update.genero
            if user_update.roles is not None:
                usuario.name = user_update.roles
        return usuario.id
        raise HTTPException(status_code=404, detail=f"Error al eliminar, id {id} falla.")
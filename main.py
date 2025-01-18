from fastapi import FastAPI

app = FastAPI()


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

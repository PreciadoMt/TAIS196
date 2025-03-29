
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modelUsuario, modelauth
from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from routers.usuarios import routerUsuario

app = FastAPI(
    title='Mi primer API 196',
    description='Preciado Martinez Uriel Ivan',
    version='1.0.1'
)

#levanta las tablas definids en los modelos
Base.metadata.create_all(bind=engine)

app.include_router(routerUsuario)

""" usuarios = [
    {"id":1, "nombre":"Preciado","edad":21, "correo":"correo@correo.com"},
    {"id":2, "nombre":"Martinez","edad":21, "correo":"correo@correo.com"},
    {"id":3, "nombre":"Uriel","edad":21, "correo":"correo@correo.com"},
    {"id":4, "nombre":"Ivan","edad":21, "correo":"correo@correo.com"}
] """

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastApi''Preciado'}



@app.post('/auth', tags=['Autentificacion'])
def login(autorizado:modelauth):
    if autorizado.corre == 'ivan@example.com' and autorizado.passw == '123456789':
        token: str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"aviso":"usuario no autorizado"}

""" #endpoint actualizar
@app.put('/usuarios/', response_model= modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]= usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


#endpoint eliminar
@app.delete('/usuarios/', tags=['Operaciones CRUD'])
def eliminar_usuario(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {"Mensaje": "Usuario eliminado con exito"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado") """

            

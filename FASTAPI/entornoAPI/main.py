from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario, modelauth
from tokenGen import createToken
from middlewares import BearerJWT



app = FastAPI(
    title='Mi primer API 196',
    description='Preciado Martinez Uriel Ivan',
    version='1.0.1'
)


usuarios = [
    {"id":1, "nombre":"Preciado","edad":21, "correo":"correo@correo.com"},
    {"id":2, "nombre":"Martinez","edad":21, "correo":"correo@correo.com"},
    {"id":3, "nombre":"Uriel","edad":21, "correo":"correo@correo.com"},
    {"id":4, "nombre":"Ivan","edad":21, "correo":"correo@correo.com"}
]

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




#endponit consultar all
@app.get('/usuarios', dependencies=[Depends(BearerJWT())] ,response_model= List[modelUsuario], tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#endopoint para agregar usuarios
@app.post('/usuarios/', response_model= modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuarionuevo.id:
            raise HTTPException(status_code= 400, details="El usuario ya existe")
    usuarios.append(usuarionuevo)
    return usuarionuevo

#endpoint actualizar
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
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

            

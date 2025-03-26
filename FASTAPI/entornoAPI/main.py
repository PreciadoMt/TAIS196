from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario, modelauth
from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User


app = FastAPI(
    title='Mi primer API 196',
    description='Preciado Martinez Uriel Ivan',
    version='1.0.1'
)
#levanta las tablas definids en los modelos
Base.metadata.create_all(bind=engine)


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
    db=Session()
    try:
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"mensaje":"Usario Guardado","usuario":usuarionuevo.model_dump() })
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"mensaje":" No se guardo nadota","Excepcion":str(e) })

    finally:
        db.close()

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

            

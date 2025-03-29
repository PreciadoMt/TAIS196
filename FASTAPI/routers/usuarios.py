from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modelUsuario, modelauth
from tokenGen import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario= APIRouter()


#dependencies=[Depends(BearerJWT())] ,response_model= List[modelUsuario], <-- ESO VA ENTRE LA LINEA DE USUARIOS Y TAGS

#endponit consultar all

@routerUsuario.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    db=Session()
    try:
        consuta=db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consuta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje":" No se puede consultaar nadota","Excepcion":str(x) })
    finally:
        db.close()
   # return usuarios  #SE QUITA PARA NO REGRESAR ESO

#endpoint para consultar ID
@routerUsuario.get('/usuarios/{id}', tags=['Operaciones CRUD'])
def ConsultarUno(id:int):
    db=Session()
    try:
        consuta=db.query(User).filter(User.id == id).first()
        if not consuta:
            return JSONResponse(satus_code=404, content={"Mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consuta))
    except Exception as x:
        return JSONResponse(status_code=500, content={"mensaje":" No se puede consultaar nadota","Excepcion":str(x) })
    finally:
        db.close()


#endopoint para agregar usuarios
@routerUsuario.post('/usuarios/', response_model= modelUsuario, tags=['Operaciones CRUD'])
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

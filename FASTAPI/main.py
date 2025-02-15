from fastapi import FastAPI, HTTPException
from typing import Optional


app = FastAPI(
    title='Mi primer API 196',
    description='Preciado Martinez Uriel Ivan',
    version='1.0.1'
)

usuarios = [
    {"id":1, "nombre":"Preciado","edad":21},
    {"id":2, "nombre":"Martinez","edad":21},
    {"id":3, "nombre":"Uriel","edad":21},
    {"id":4, "nombre":"Ivan","edad":21}
]

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastApi''Preciado'}

#endponit consultar all
@app.get('/usuarios', tags=['Operaciones CRUD'])
def ConsultarTodos():
    return{"Usiarios Registrados": usuarios}

#endopoint para agregar usuarios
@app.post('/usuarios/',tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo:dict):
    for usr in usuarios:
        if usr["id"] == usuarionuevo.get("id"):
            raise HTTPException(status_code= 400, details="El usuario ya existe")

    usuarios.append(usuarionuevo)
    return usuarionuevo
#Creee este coso para poder decir que hcie cambios
#endpoint actualizar
@app.put('/usuarios/', tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

#Creee este coso para poder decir que hcie cambios x300 
#endpoint eliminar
@app.delete('/usuarios/', tags=['Operaciones CRUD'])
def eliminar_usuario(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {"Mensaje": "Usuario eliminado con exito"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

            

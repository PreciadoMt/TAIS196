from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from datetime import date

app = FastAPI(
    title='Gestor de Tareas',
    description='API para gestionar una lista de tareas',
    version='1.0.0'
)

# Modelo de datos para las tareas
class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    vencimiento: str
    estado: str

# BD FAKE 
tareas: List[Tarea] = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "14-02-24",
        "estado": "completada"
    }
]

@app.get('/', tags=['Inicio'])
def main():
    return {'mensaje': 'Bienvenido a la API de Gestión de Tareas'}

# Consultar tareas
@app.get('/tareas', tags=['Operaciones CRUD'])
def consultar_todas():
    return {'Tareas Registradas': tareas}

# Agregar tarea
@app.post('/tareas/', tags=['Operaciones CRUD'])
def agregar_tarea(tarea_nueva: Tarea):
    for tarea in tareas:
        if tarea["id"] == tarea_nueva.id:
            raise HTTPException(status_code=400, detail="La tarea ya existe")
    
    tareas.append(tarea_nueva.dict())
    return tarea_nueva

# Actualizar tarea
@app.put('/tareas/', tags=['Operaciones CRUD'])
def actualizar_tarea(id: int, tarea_actualizada: Tarea):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas[index] = tarea_actualizada.dict()
            return tareas[index]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Eliminar una tarea
@app.delete('/tareas/', tags=['Operaciones CRUD'])
def eliminar_tarea(id: int):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            del tareas[index]
            return {"mensaje": "Tarea eliminada con éxito"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
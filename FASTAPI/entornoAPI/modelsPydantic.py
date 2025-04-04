from pydantic import BaseModel, Field, EmailStr


#Modelo para validacion de datos
class modelUsuario(BaseModel):
    name: str = Field(...,min_length=3, max_length=15, description="solo letras y de un rango de 3 a 15 caracteres ")
    age: int = Field(..., gt=0, le=130, description="La edad debe ser mayor a 0 y menor o igual a 130 años.")
    email: EmailStr= Field(...,example="texto@texto.com", description="Debe ser una dirección de correo electrónico válida.")

class modelauth(BaseModel):
    corre:EmailStr
    passw:str = Field(..., min_length=8, strip_whitespace=True, description="contraseña minimo 8 caracteres")


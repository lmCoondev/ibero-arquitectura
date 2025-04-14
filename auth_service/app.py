from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Middleware para habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definimos el modelo para el login
class LoginRequest(BaseModel):
    usuario: str
    clave: str

# Lista de usuarios para validación
usuarios = [{"usuario": "admin", "clave": "1234"}]

@app.post("/login")
async def login(request: LoginRequest):
    # Verificamos las credenciales
    for u in usuarios:
        if u["usuario"] == request.usuario and u["clave"] == request.clave:
            return {"estado": "exitoso"}
    
    # Si no se encuentran coincidencias, retornamos un error
    raise HTTPException(status_code=401, detail="Usuario o clave incorrectos")

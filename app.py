# Práctica 4 - Comunicación entre contenedores
# Alumno: Erick Alejandro Contreras Salas
# Expediente: 722185
# Desarrollo en la Nube - Primavera 2026 ITESO

from fastapi import FastAPI
from app.services.boletin_services import create_boletin

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola desde el contenedor de FastAPI!"}

@app.post("/boletines/{boletin_id}")
def create_boletin_endpoint(boletin_id: int, boletin_message: str, boletin_file: bytes, email: str):
    return create_boletin(boletin_id, boletin_message, boletin_file, email)

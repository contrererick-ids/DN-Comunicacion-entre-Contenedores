# Definición de las funciones que manejan los boletines

def create_boletin(boletin_id: int, boletin_message: str, boletin_file: bytes, email: str):
    return {
        "boletin_id": boletin_id,
        "message": boletin_message,
        "file_size": len(boletin_file),
        "email": email,
        "status": "Boletín creado exitosamente"
    }

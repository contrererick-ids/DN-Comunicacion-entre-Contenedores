# Definición de las funciones que manejan los boletines

boletin_list = []  # Lista para almacenar los boletines (puedes reemplazar esto con una base de datos)

def create_boletin(boletin_id: int, boletin_message: str, boletin_file: bytes, email: str):
    for boletin in boletin_list:
        if boletin["boletin_id"] == boletin_id:
            return {"error": "El boletín con este ID ya existe."}
    boletin_data = {
        "boletin_id": boletin_id,
        "message": boletin_message,
        "file_size": len(boletin_file),
        "email": email
    }
    boletin_list.append(boletin_data)
    return {
        "boletin_id": boletin_id,
        "message": boletin_message,
        "file_size": len(boletin_file),
        "email": email,
        "status": "Boletín creado exitosamente"
    }

def get_boletin_by_ID(boletin_id: int):
    for boletin in boletin_list:
        if boletin["boletin_id"] == boletin_id:
            return boletin
    return {"error": "Boletín no encontrado."}
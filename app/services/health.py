from app.schemas.blacklist import GenericResponse

def check_health():
    return GenericResponse(msg="Este servicio está funcionando correctamente.")

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_example():
    return {"msg": "Hola desde el endpoint example"}

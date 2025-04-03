from fastapi import APIRouter, status

from app.schemas.blacklist import GenericResponse
from app.services.health import check_health

router = APIRouter()

@router.get(
    "/health",
    name="Check health service",
    description="Check the health of the microservice.",
    status_code=status.HTTP_200_OK,
    response_model=GenericResponse,
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": GenericResponse}
    }
)
def get_health():
    response = check_health()
    return response.model_dump()
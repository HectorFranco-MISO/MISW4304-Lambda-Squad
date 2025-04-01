from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import JSONResponse

from app.api.v1.utils.token_handler import TokenValidator
from app.schemas.blacklist import BlacklistRequest, GenericResponse, GetBlacklistResponse
from app.services.blacklist import add_to_blacklist, check_email
from app.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post(
    "/",
    name="Add e-mail to Blacklist",
    description="Add an e-mail to the Blacklist",
    dependencies=[Depends(TokenValidator())],
    status_code=status.HTTP_201_CREATED)
def blacklist_email(
        payload: BlacklistRequest,
        request: Request,
        db: Session = Depends(get_db)
):
    client_ip = request.client.host
    entry = add_to_blacklist(db, payload, client_ip)
    return JSONResponse(content={
        "id": str(entry.id),
        "email": entry.email,
        "app_uuid": str(entry.app_uuid),
        "reason": entry.blocked_reason,
        "ip_address": entry.ip_address,
        "created_at": entry.created_at.isoformat()
    })


@router.get(
    "/{email}",
    name="Check Blacklist",
    description="Check if an email is blacklisted.",
    dependencies=[Depends(TokenValidator())],
    status_code=status.HTTP_200_OK,
    response_model=GetBlacklistResponse,
    responses={
        status.HTTP_403_FORBIDDEN: {"model": GenericResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": GenericResponse}
    }
)
def get_blacklist(email: str, db: Session = Depends(get_db)):
    response = check_email(db, email)
    return response.model_dump()

from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import JSONResponse
from app.schemas.blacklist import BlacklistRequest
from app.services.blacklist import add_to_blacklist
from app.dependencies import get_db 
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
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
        "client_id": str(entry.client_id),
        "reason": entry.reason,
        "ip_address": entry.ip_address,
        "created_at": entry.created_at.isoformat()
    })

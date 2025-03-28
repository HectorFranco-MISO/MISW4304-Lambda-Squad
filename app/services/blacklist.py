from datetime import datetime
from app.models.blacklist import BlacklistedEmail
from app.schemas.blacklist import BlacklistRequest
from sqlalchemy.orm import Session

def add_to_blacklist(db: Session, data: BlacklistRequest, ip_address: str):
    entry = BlacklistedEmail(
        email=data.email,
        client_id=data.client_id,
        reason=data.reason,
        ip_address=ip_address,
        created_at=datetime.utcnow()
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

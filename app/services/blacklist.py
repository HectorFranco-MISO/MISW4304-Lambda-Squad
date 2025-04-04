from datetime import datetime, timezone
from app.models.blacklist import BlacklistedEmail
from app.schemas.blacklist import BlacklistRequest, GetBlacklistResponse
from sqlalchemy.orm import Session


def add_to_blacklist(db: Session, data: BlacklistRequest, ip_address: str):
    entry = BlacklistedEmail(
        email=str(data.email),
        app_uuid=data.app_uuid,
        blocked_reason=data.blocked_reason,
        ip_address=ip_address,
        created_at=datetime.now(timezone.utc)
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def check_email(db: Session, email: str):
    entry = db.query(BlacklistedEmail).filter(BlacklistedEmail.email == email).first()
    if entry:
        return GetBlacklistResponse(blacklisted=True, blocked_reason=str(entry.blocked_reason))
    else:
        return GetBlacklistResponse(blacklisted=False)

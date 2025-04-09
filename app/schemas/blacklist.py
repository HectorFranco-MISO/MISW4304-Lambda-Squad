from pydantic import BaseModel, EmailStr, UUID4, constr
from typing import Optional


class BlacklistRequest(BaseModel):
    email: EmailStr
    app_uuid: str
    blocked_reason: Optional[constr(max_length=255)] = None


class GetBlacklistResponse(BaseModel):
    blacklisted: bool
    blocked_reason: Optional[str] = None


class GenericResponse(BaseModel):
    msg: str

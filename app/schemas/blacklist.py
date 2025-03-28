from pydantic import BaseModel, EmailStr, UUID4, constr
from typing import Optional

class BlacklistRequest(BaseModel):
    email: EmailStr
    client_id: UUID4
    reason: Optional[constr(max_length=255)] = None

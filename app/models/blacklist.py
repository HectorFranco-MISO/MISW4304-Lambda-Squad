import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.db import Base  

class BlacklistedEmail(Base):
    __tablename__ = "blacklist"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False)
    client_id = Column(UUID(as_uuid=True), nullable=False)
    reason = Column(String(255), nullable=True)
    ip_address = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

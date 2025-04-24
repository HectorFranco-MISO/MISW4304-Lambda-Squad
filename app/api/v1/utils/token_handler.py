import os

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.development')

TOKEN = os.getenv("SECRET_TOKEN", "bGFtYmRhX3NxdWFk")

class TokenValidator(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(TokenValidator, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials = await super().__call__(request)
        if not credentials or credentials.scheme != "Bearer" or credentials.credentials != TOKEN:
            raise HTTPException(status_code=403, detail="El token no es válido.")

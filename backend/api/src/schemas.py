from pydantic import BaseModel

class AuthDetails(BaseModel):
    user: str
    password: str
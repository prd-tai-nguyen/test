from typing import Optional

from pydantic import BaseModel


class EnvBase(BaseModel):
    client_id: Optional[str]
    client_secret: Optional[str]
    api_url: Optional[str]


class EnvCreate(EnvBase):
    client_id: str
    client_secret: str
    api_url: str

class EnvUpdate(EnvBase):
    client_secret: str
    api_url: str

class EnvResponse(EnvBase):
    id: int
    
    class Config:
        orm_mode = True
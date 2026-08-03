from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class GameForm(BaseModel):
    title: str 
    description: str 
    version: str 
    url_download: str


class GameDB(BaseModel):
    id: str
    title: str 
    description: str
    version: str 
    created_at: str
    likes_count: int
    url_download: str
    owner_id: int
    
     
class VideogameResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str 
    description: str
    version: str 
    created_at: datetime
    likes_count: int
    url_download: str


class VideogameUpgrade(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    version: Optional[str] = None
    url_download: Optional[str] = None
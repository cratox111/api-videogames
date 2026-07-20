from pydantic import BaseModel

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
    
     
    
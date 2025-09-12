from pydantic import BaseModel

class Voice(BaseModel):
    id: str
    name: str
    preview_url: str
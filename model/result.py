from pydantic import BaseModel

class Result(BaseModel):
    id: int
    text: str
    audio_name: str
    created_at: str
    updated_at: str
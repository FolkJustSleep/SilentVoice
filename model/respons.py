from pydantic import BaseModel

class ResponseModel(BaseModel):
    status: str
    message: str
    result: str | None = None
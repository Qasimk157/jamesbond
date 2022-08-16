from pydantic import BaseModel


class ResponseMessage(BaseModel):
    success: bool
    message: str

from fastapi_camelcase import CamelModel


class UnauthorizedResponse(CamelModel):
    status: bool
    message: str

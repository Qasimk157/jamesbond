from fastapi_camelcase import CamelModel


class TextToSpeechResponsePayload(CamelModel):
    id: str
    enter_text: str

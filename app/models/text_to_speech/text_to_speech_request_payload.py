from fastapi_camelcase import CamelModel


class TextToSpeechRequestPayload(CamelModel):
    enter_text: str

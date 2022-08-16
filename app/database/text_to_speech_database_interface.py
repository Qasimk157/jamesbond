
from abc import abstractmethod

from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from interface import Interface


class ITextToSpeechDatabase(Interface):
    @abstractmethod
    async def create(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        pass

    async def get_queury_if_exist_in_database(self, enterText: str):
        pass
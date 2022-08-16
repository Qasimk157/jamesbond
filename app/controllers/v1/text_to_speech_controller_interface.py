
from abc import abstractmethod

from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from interface import Interface


class ITextToSpeechController(Interface):

    @abstractmethod
    async def create_by_tts(self, request_payload: TextToSpeechRequestPayload):
        pass
    
    @abstractmethod
    async def create_by_gTTS(self, request_payload: TextToSpeechRequestPayload):
        pass



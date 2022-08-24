from app.controllers.v1.text_to_speech_controller_interface import \
    ITextToSpeechController
from app.core.text_to_speech_manager import TextToSpeechManager
from app.models.error_messages import ErrorMessages
from app.models.logger import Logger
from app.models.response_message import ResponseMessage
from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from app.models.text_to_speech.text_to_speech_response_payload import \
    TextToSpeechResponsePayload
from app.models.unauthorized_response import UnauthorizedResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
import pyttsx3
from fastapi_utils.inferring_router import InferringRouter
from interface import implements

router = InferringRouter()


@cbv(router)
class TextToSpeechControllerController(implements(ITextToSpeechController)):
    def __init__(self):
        self.manager = TextToSpeechManager()
        self.logger = Logger()

    @router.post("/by-pyttsx3/",
                 summary="Create a text to speech response",
                 description="return text to speech response",
                 status_code=status.HTTP_201_CREATED,
                 response_model=TextToSpeechResponsePayload,
                 responses={status.HTTP_400_BAD_REQUEST: {"model": ResponseMessage},
                            status.HTTP_401_UNAUTHORIZED: {"model": UnauthorizedResponse},
                            status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ResponseMessage},
                            status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ResponseMessage}})
    async def create_by_tts(self, request_payload: TextToSpeechRequestPayload):
        try:
            
            engine = pyttsx3.init()
            engine.setProperty('rate', 125)
            engine.setProperty('volume',1.0)  
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(request_payload.enter_text)
            engine.save_to_file(request_payload.enter_text, 'pyttsx.mp3')
            engine.runAndWait()
            engine.stop()
            
            
            response = request_payload.dict()
            # response = await self.manager.create_by_tts(request_payload)
            if not isinstance(response, ResponseMessage):
                return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(response))
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=jsonable_encoder(response))
        except Exception as e:
            self.logger.error(e)
            message = ResponseMessage(
                success=False, message=ErrorMessages.server_error.value)
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder(message))
            return response
        
    
    @router.post("/by-ruth-text-to-speech/",
                 summary="Create a text to speech response",
                 description="return text to speech response",
                 status_code=status.HTTP_201_CREATED,
                 response_model=TextToSpeechResponsePayload,
                 responses={status.HTTP_400_BAD_REQUEST: {"model": ResponseMessage},
                            status.HTTP_401_UNAUTHORIZED: {"model": UnauthorizedResponse},
                            status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ResponseMessage},
                            status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ResponseMessage}})
    async def create_by_gTTS(self, request_payload: TextToSpeechRequestPayload):
        try:
            
            engine = pyttsx3.init()
            engine.setProperty('rate', 125)
            engine.setProperty('volume',1.0)  
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(request_payload.enter_text)
            engine.save_to_file(request_payload.enter_text, 'pyttsx.mp3')
            engine.runAndWait()
            engine.stop()
            
            
            response = request_payload.dict()
            
            # response = await self.manager.create_by_gTTS(request_payload)
            if not isinstance(response, ResponseMessage):
                return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(response))
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=jsonable_encoder(response))
        except Exception as e:
            self.logger.error(e)
            message = ResponseMessage(
                success=False, message=ErrorMessages.server_error.value)
            response = JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder(message))
            return response

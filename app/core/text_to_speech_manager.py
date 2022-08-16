from app.core.text_to_speech_manager_interface import ITextToSpeechManager
from app.database.text_to_speech_database import TextToSpeechDatabase
from app.models.logger import Logger
from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from app.models.text_to_speech.text_to_speech_response_payload import \
    TextToSpeechResponsePayload
from fastapi.encoders import jsonable_encoder
import pyttsx3
from interface import implements


class TextToSpeechManager(implements(ITextToSpeechManager)):
    def __init__(self):
        self.database = TextToSpeechDatabase()
        self.logger = Logger()

    async def create_by_tts(self, request_payload: TextToSpeechRequestPayload):
        
        create_text_to_speech_request = jsonable_encoder(
            request_payload)
        database_testing_duplication = await self.database.get_queury_if_exist_in_database(request_payload.enter_text)
        if database_testing_duplication:
            database_testing_duplication["id"] = str(database_testing_duplication["_id"])
            data_recieved = TextToSpeechResponsePayload(**database_testing_duplication)
            print(data_recieved.enter_text)
            
            engine = pyttsx3.init()
            engine.setProperty('rate', 125)
            engine.setProperty('volume',1.0)  
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(data_recieved.enter_text)
            engine.save_to_file(data_recieved.enter_text, 'pyttsx.mp3')
            engine.runAndWait()
            engine.stop()
        
            data_recieved.id = database_testing_duplication["id"]
            return data_recieved
        response = await self.database.create(create_text_to_speech_request)
        
        response["id"] = str(response["_id"])
        api_response = TextToSpeechResponsePayload(**response)
        
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume',1.0)  
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(api_response.enter_text)
        engine.save_to_file(api_response.enter_text, 'pyttsx.mp3')
        engine.runAndWait()
        engine.stop()
        
        api_response.id = response["id"]
        return api_response
    
    
    async def create_by_gTTS(self, request_payload: TextToSpeechRequestPayload):
        
        create_text_to_speech_request = jsonable_encoder(
            request_payload)
        
        
        database_testing_duplication = await self.database.get_queury_if_exist_in_database(request_payload.enter_text)
        if database_testing_duplication:
            database_testing_duplication["id"] = str(database_testing_duplication["_id"])
            data_recieved = TextToSpeechResponsePayload(**database_testing_duplication)
            print(data_recieved.enter_text)
            
            engine = pyttsx3.init()
            engine.setProperty('rate', 125)
            engine.setProperty('volume',1.0)  
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(data_recieved.enter_text)
            engine.save_to_file(data_recieved.enter_text, 'pyttsx.mp3')
            engine.runAndWait()
            engine.stop()
        
            data_recieved.id = database_testing_duplication["id"]
            return data_recieved
        
        response = await self.database.create(create_text_to_speech_request)
        
        response["id"] = str(response["_id"])
        api_response = TextToSpeechResponsePayload(**response)

        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume',1.0)  
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(api_response.enter_text)
        engine.save_to_file(api_response.enter_text, 'pyttsx.mp3')
        engine.runAndWait()
        engine.stop()
        
        api_response.id = response["id"]
        return api_response
    
import asyncio

# from app.config.config import MONGODB_CON_STR
from app.database.text_to_speech_database_interface import \
    ITextToSpeechDatabase
from pymongo import MongoClient
from app.models.text_to_speech.text_to_speech_request_payload import \
    TextToSpeechRequestPayload
from fastapi.encoders import jsonable_encoder
from interface import implements
from motor.motor_asyncio import AsyncIOMotorClient


class TextToSpeechDatabase(implements(ITextToSpeechDatabase)):
    # print(MONGODB_CON_STR)
    cluster = MongoClient("mongodb+srv://qasim:qasim@cluster0.cyxbnuq.mongodb.net/?retryWrites=true&w=majority")
    db = cluster["text_to_speech"]
    text_to_speech_collection = db["text"]
    # client = AsyncIOMotorClient(MONGODB_CON_STR)
    # client.get_io_loop = asyncio.get_running_loop
    # text_to_speech_collection = client[DATABASE_NAME]["text_to_speech"]
    # category_history_collection = client[DATABASE_NAME]["history_text_to_speech"]

    async def create(self, text_to_speech_request_paylad: TextToSpeechRequestPayload):
        document = jsonable_encoder(text_to_speech_request_paylad)
        result = self.text_to_speech_collection.insert_one(document)
        document["_id"] = result.inserted_id
        return document
    
    async def get_queury_if_exist_in_database(self, enterText: str):
        data =  self.text_to_speech_collection.find_one({"enterText": enterText})
        print(data)
        return data


from app.controllers.v1.text_to_speech_controller import router as text_to_speech_router
from fastapi import APIRouter

API_V1_STR = "/v1"

router = APIRouter()
router.include_router(text_to_speech_router, tags=[
                      "Text to Speech Controller"], prefix=f'{API_V1_STR}/text/speech') #dependencies=[Depends(JWTAuthentication())])
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.controllers.router import router

app = FastAPI(prefix="/v1/")
app.include_router(router)
origins = ["http://localhost:4000", ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
add_pagination(app)


@app.get("/")
async def get_root():
    return {"message": "Text to Speech APIs version 0.1.0"}

# web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
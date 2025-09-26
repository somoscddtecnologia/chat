# app/main.py

from fastapi import FastAPI
from .routes import http, websocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chat com websocket e Histórico no MongoDB")

origins = [
    "http://127.0.0.1:5500",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(http.router)
app.include_router(websocket.router) 
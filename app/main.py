# app/main.py

from fastapi import FastAPI
from .routes import http, websocket

app = FastAPI(title="Chat com websocket e Histórico no MongoDB")

app.include_router(http.router)
app.include_router(websocket.router) 
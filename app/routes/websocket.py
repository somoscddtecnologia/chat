# app/routes/websocket.py
from fastapi import APIRouter, WebSocket
from ..manager import manager

router = APIRouter()

@router.websocket("/ws/{sala_id}") # faltava /
async def websocket_endpoint(websocket: WebSocket, sala_id: str, nickname: str = "Anônimo"):
    await manager.connect(sala_id, websocket, nickname)


    return True
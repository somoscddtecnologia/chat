# app/routes/websocket.py
from fastapi import APIRouter, WebSocket
from ..manager import manager
from ..database import salvar_mensagem

router = APIRouter()

@router.websocket("/ws/{sala_id}") # faltava /
async def websocket_endpoint(websocket: WebSocket, sala_id: str, nickname: str = "Anônimo"):
    await manager.connect(sala_id, websocket, nickname)
    await manager.broadcast(sala_id, f"[sistema] Usuários na sala {sala_id}: ");# adicionar pela lista

    while True:
        data = await websocket.receive_text()

        
        await salvar_mensagem(sala_id, nickname, data)

# app/routes/websocket.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..manager import manager
from ..database import salvar_mensagem, pegar_historico

router = APIRouter()

@router.websocket("/ws/{sala_id}") # faltava /
async def websocket_endpoint(websocket: WebSocket, sala_id: str, nickname: str = "Anônimo"):
    await manager.connect(sala_id, websocket, nickname)

    try:
        #quando alguém entrar na sala
        await manager.broadcast(sala_id, f"[sistema] {nickname} entrou na sala {sala_id}.")

        #atualizando a lista de usuários
        usuarios = await manager.list_users(sala_id)
        await manager.broadcast(sala_id, f"[sistema] Usuários na sala {sala_id}: " . join(usuarios));# adicionar pela lista
        
        historico = await pegar_historico(sala_id)
        for mensagem in historico:
            await websocket.send_text(f"{mensagem['nickname']}: {mensagem['mensagem']}")

        while True:
            data = await websocket.receive_text()
            await salvar_mensagem(sala_id, nickname, data)
    
    except WebSocketDisconnect:
        await manager.disconnect(sala_id, websocket)
    

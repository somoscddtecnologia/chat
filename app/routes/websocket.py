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
        await manager.broadcast(sala_id, f"[sistema] novo usuário: {nickname} entrou na sala {sala_id}.")

        #atualizando a lista de usuários
        usuarios = await manager.list_users(sala_id)
        await manager.broadcast(sala_id, f"[sistema] Usuários na sala {sala_id}: {', '.join(usuarios)}")
        
        #enviar histórico apenas para quem entrar
        historico = await pegar_historico(sala_id)
        for mensagem in historico:
            await websocket.send_text(f"{mensagem['nickname']}: {mensagem['mensagem']}")

        while True:
            data = await websocket.receive_text()

            if data.strip() == "/usuarios":
                usuarios = await manager.list_users(sala_id)
                await websocket.send_text(f"[sistema] Usuários da sala {sala_id}: {', ' . join(usuarios)}")
            else:
                await salvar_mensagem(sala_id, nickname, data)
                await manager.broadcast(sala_id, f"{nickname}: {data}")
    
    except WebSocketDisconnect:
        #sinal de desconexão
        await manager.disconnect(sala_id, websocket)

        #envia mensagem para todos
        await manager.broadcast(sala_id, f"[sistema] {nickname} saiu da {sala_id}.")

        #atualizando a lista de usuários
        usuarios = await manager.list_users(sala_id)
        await manager.broadcast(sala_id, f"[sistema] Usuários na sala {sala_id}: " . join(usuarios)); 
      
    

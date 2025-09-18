# app/manager.py
from fastapi import WebSocket
from typing import Dict, List
import asyncio

class ConnectionManager:
    def __init__(self):
        self.salas: Dict[str, Dict[WebSocket, str]] = {}
        self.lock: asyncio.Lock()
    
    async def connect(self, sala_id: str, websocket: WebSocket, nickname: str):
        await websocket.accept()
        async with self.lock:
            if sala_id not in self.salas:
                self.salas[sala_id] = {}
            self.salas[sala_id][websocket] = nickname
    
    async def disconnect(self, sala_id: str, websocket: WebSocket):
        async with self.lock:
            if sala_id in self.salas and websocket in self.salas[sala_id]:
                del self.salas[sala_id][websocket]
                if not self.salas[sala_id]:
                    del self.salas[sala_id]

    async def list_users(self, sala_id: str) -> List[str]:
        async with self.lock:
            if sala_id in self.salas:
                return list(self.salas[sala_id].values)
            return []    

#inicializando
manager = ConnectionManager()
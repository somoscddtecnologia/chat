# app/database.py

from pymongo import MongoClient, ASCENDING
from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGOURL, MONGODB 

#client = MongoClient(MONGOURL)
client = AsyncIOMotorClient(MONGOURL)
db = client[MONGODB]
mensagens = db["mensagens"]
usuarios = db["usuarios"]

from datetime import datetime

async def salvar_mensagem(sala_id: str, nickname: str, mensagem: str):
    mensagens.insert_one(
        {  
            "sala_id": sala_id,
            "nickname": nickname,
            "mensagem": mensagem,
            "timestamp": datetime.utcnow()
        }
        )

async def pegar_historico(sala_id: str, limite: int = 5):
    dados = mensagens.find({"sala_id": sala_id}).sort("_id", ASCENDING).limit(limite)
    return [doc async for doc in dados]
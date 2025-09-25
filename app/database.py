# app/database.py

from pymongo import MongoClient, ASCENDING, DESCENDING
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

async def pegar_historico(sala_id: str, limite: int = 10):
    dados = mensagens.find({"sala_id": sala_id}).sort("_id", DESCENDING).limit(limite)
    docs = [doc async for doc in dados]
    return list(reversed(docs))
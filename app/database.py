# app/database.py

from pymongo import MongoClient
from .config import MONGOURL, MONGODB 

client = MongoClient(MONGOURL)
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

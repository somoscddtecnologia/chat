# app/routes/http.py

from fastapi import APIRouter
from ..manager import ConnectionManager
#from ..database import get_history
from ..database import salvar_mensagem


router = APIRouter()
manager = ConnectionManager()

@router.get("/")
async def root():
    return {"message": "Bem-vindo! Conecte-se em /ws/{sala_id}?nickname=SeuNome"}

@router.get("/salas")
async def list_salas():
    return {sala_id: list(nicks.values()) for sala_id, nicks in manager.salas.items()}

@router.get("/historico/{sala_id}")
async def history(sala_id: str):
    return {"message": "Aqui teremos o histórico"}


@router.get("/teste")
async def teste():
    salvar_mensagem(1, "carlosh", "oi oi oi sadsadsad")

    return {"message": "Aqui teremos o histórico"}
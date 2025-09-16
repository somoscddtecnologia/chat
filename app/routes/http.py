# app/routes/http.py

from fastapi import APIRouter
#from ..manager import ConnectionManager
#from ..database import get_history
from ..database import salvar_mensagem


router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Bem-vindo! Conecte-se em /ws/{sala_id}?nickname=SeuNome"}

@router.get("/salas")
async def list_salas():
    return {"message": "Aqui teremos as salas"}

@router.get("/historico/{sala_id}")
async def history(sala_id: str):
    return {"message": "Aqui teremos o histórico"}


@router.get("/teste")
async def teste():
    salvar_mensagem(1, "carlosh", "oi oi oi ")

    return {"message": "Aqui teremos o histórico"}
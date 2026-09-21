from fastapi import FastAPI
from pydantic import BaseModel

from servidor import Servidor
from gerenciador import Gerenciador
from banco import Base, engine, SessaoLocal
from modelo import ServidorModelo

import modelo


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud Resource Manager")
gerenciador = Gerenciador()


class ServidorEntrada(BaseModel):
    identificador: int
    nome: str
    ip: str
    sistema: str


@app.get("/")
def inicio():
    return {"mensagem": "Cloud Resource Manager Online"}


@app.post("/servidores")
def criar_servidor(dados: ServidorEntrada):
    banco = SessaoLocal()

    servidor = ServidorModelo(
        identificador=dados.identificador,
        nome=dados.nome,
        ip=dados.ip,
        sistema=dados.sistema,
        status="Desligado"
    )

    banco.add(servidor)
    banco.commit()
    banco.refresh(servidor)
    banco.close()

    return {
        "mensagem": "Servidor criado com sucesso",
        "identificador": servidor.identificador
    }

@app.get("/servidores")
def listar_servidores():
    banco = SessaoLocal()

    servidores = banco.query(ServidorModelo).all()

    banco.close()

    return servidores
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from banco import Base, engine, SessaoLocal
from modelo import ServidorModelo


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud Resource Manager")


class ServidorEntrada(BaseModel):
    identificador: int
    nome: str
    ip: str
    sistema: str


class ServidorAtualizacao(BaseModel):
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


@app.get("/servidores/{identificador}")
def buscar_servidor(identificador: int):
    banco = SessaoLocal()
    servidor = banco.get(ServidorModelo, identificador)
    banco.close()

    if servidor is None:
        raise HTTPException(
            status_code=404,
            detail="Servidor não encontrado"
        )

    return servidor


@app.put("/servidores/{identificador}")
def atualizar_servidor(
    identificador: int,
    dados: ServidorAtualizacao
):
    banco = SessaoLocal()
    servidor = banco.get(ServidorModelo, identificador)

    if servidor is None:
        banco.close()
        raise HTTPException(
            status_code=404,
            detail="Servidor não encontrado"
        )

    servidor.nome = dados.nome
    servidor.ip = dados.ip
    servidor.sistema = dados.sistema

    banco.commit()
    banco.refresh(servidor)
    banco.close()

    return servidor


@app.delete("/servidores/{identificador}")
def remover_servidor(identificador: int):
    banco = SessaoLocal()
    servidor = banco.get(ServidorModelo, identificador)

    if servidor is None:
        banco.close()
        raise HTTPException(
            status_code=404,
            detail="Servidor não encontrado"
        )

    banco.delete(servidor)
    banco.commit()
    banco.close()

    return {"mensagem": "Servidor removido com sucesso"}


@app.post("/servidores/{identificador}/iniciar")
def iniciar_servidor(identificador: int):
    banco = SessaoLocal()
    servidor = banco.get(ServidorModelo, identificador)

    if servidor is None:
        banco.close()
        raise HTTPException(
            status_code=404,
            detail="Servidor não encontrado"
        )

    servidor.status = "Ligado"

    banco.commit()
    banco.refresh(servidor)
    banco.close()

    return servidor


@app.post("/servidores/{identificador}/parar")
def parar_servidor(identificador: int):
    banco = SessaoLocal()
    servidor = banco.get(ServidorModelo, identificador)

    if servidor is None:
        banco.close()
        raise HTTPException(
            status_code=404,
            detail="Servidor não encontrado"
        )

    servidor.status = "Desligado"

    banco.commit()
    banco.refresh(servidor)
    banco.close()

    return servidor
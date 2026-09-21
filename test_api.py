from fastapi.testclient import TestClient

from api import app


cliente = TestClient(app)


def test_api_online():
    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert resposta.json() == {
        "mensagem": "Cloud Resource Manager Online"
    }


def test_servidor_inexistente():
    resposta = cliente.get("/servidores/999999")

    assert resposta.status_code == 404
    assert resposta.json() == {
        "detail": "Servidor não encontrado"
    }
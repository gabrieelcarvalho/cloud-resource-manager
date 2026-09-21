# ☁️ Cloud Resource Manager

API REST desenvolvida em Python para gerenciamento de recursos de servidores em nuvem.

O projeto permite cadastrar, consultar, atualizar e remover servidores, além de controlar seu estado entre ligado e desligado. Os dados são armazenados de forma persistente utilizando SQLite e SQLAlchemy.

## 🚀 Funcionalidades

* Cadastro de servidores
* Listagem de servidores
* Busca de servidor por identificador
* Atualização de informações
* Remoção de servidores
* Inicialização de servidores
* Desligamento de servidores
* Persistência de dados
* Tratamento de erros HTTP
* Testes automatizados

## 🛠️ Tecnologias

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Pytest
* Docker
* GitHub Actions

## 📡 API

A aplicação disponibiliza os seguintes endpoints:

| Método   | Endpoint                              | Descrição                     |
| -------- | ------------------------------------- | ----------------------------- |
| `GET`    | `/`                                   | Verifica se a API está online |
| `POST`   | `/servidores`                         | Cadastra um servidor          |
| `GET`    | `/servidores`                         | Lista os servidores           |
| `GET`    | `/servidores/{identificador}`         | Busca um servidor             |
| `PUT`    | `/servidores/{identificador}`         | Atualiza um servidor          |
| `DELETE` | `/servidores/{identificador}`         | Remove um servidor            |
| `POST`   | `/servidores/{identificador}/iniciar` | Liga um servidor              |
| `POST`   | `/servidores/{identificador}/parar`   | Desliga um servidor           |

A documentação interativa da API é disponibilizada automaticamente pelo Swagger através de:

`/docs`

## 📦 Executando o projeto

Clone o repositório:

```bash
git clone https://github.com/gabrieelcarvalho/cloud-resource-manager.git
cd cloud-resource-manager
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
python -m uvicorn api:app --reload
```

A aplicação ficará disponível em:

`http://127.0.0.1:8000`

A documentação Swagger estará em:

`http://127.0.0.1:8000/docs`

## 🧪 Testes

Os testes automatizados foram desenvolvidos com Pytest.

Para executá-los:

```bash
pytest -v
```

O projeto também utiliza GitHub Actions para executar os testes automaticamente durante o processo de integração contínua.

## 🐳 Docker

Também é possível executar a aplicação em um container Docker.

Construa a imagem:

```bash
docker build -t cloud-resource-manager .
```

Execute o container:

```bash
docker run -p 8000:8000 cloud-resource-manager
```

Depois, acesse:

`http://localhost:8000/docs`

## 📂 Estrutura

```text
cloud-resource-manager/
├── .github/
│   └── workflows/
│       └── testes.yml
├── api.py
├── banco.py
├── modelo.py
├── servidor.py
├── gerenciador.py
├── test_api.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🎯 Objetivo

O Cloud Resource Manager foi desenvolvido como projeto de estudo e portfólio, aplicando conceitos de desenvolvimento backend e cloud, como APIs REST, orientação a objetos, persistência de dados, testes automatizados, containerização e integração contínua.

## 👨‍💻 Autor

Desenvolvido por Gabriel Carvalho.

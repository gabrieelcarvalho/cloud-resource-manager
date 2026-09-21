from sqlalchemy import Column, Integer, String

from banco import Base


class ServidorModelo(Base):
    __tablename__ = "servidores"

    identificador = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ip = Column(String, nullable=False, unique=True)
    sistema = Column(String, nullable=False)
    status = Column(String, nullable=False, default="Desligado")
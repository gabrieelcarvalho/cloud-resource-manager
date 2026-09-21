from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


URL_BANCO = "sqlite:///./cloud.db"

engine = create_engine(
    URL_BANCO,
    connect_args={"check_same_thread": False}
)

SessaoLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
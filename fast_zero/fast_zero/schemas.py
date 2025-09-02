from datetime import date

from pydantic import BaseModel, ConfigDict


class Message(BaseModel):
    message: str


class DoenteSchema(BaseModel):
    numero_processo: int
    nome: str
    data_nascimento: date
    genero: str
    morada: str | None = None


class DoentePublic(BaseModel):
    nome: str
    morada: str | None = None

    # allow creating from SQLAlchemy model instances
    model_config = ConfigDict(from_attributes=True)

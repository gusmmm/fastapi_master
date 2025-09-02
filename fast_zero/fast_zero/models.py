from sqlalchemy import Column, Date, Integer, String

from fast_zero.database import Base


class Doente(Base):
    __tablename__ = "doentes"

    numero_processo = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)  # date field
    genero = Column(String, nullable=False)
    morada = Column(String, index=True, nullable=True)

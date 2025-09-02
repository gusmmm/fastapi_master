from contextlib import asynccontextmanager
from datetime import date as _date
from http import HTTPStatus

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from fast_zero.database import Base, engine, get_db
from fast_zero.models import Doente
from fast_zero.schemas import DoentePublic, DoenteSchema, Message


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure tables exist
    Base.metadata.create_all(bind=engine)
    try:
        yield
    finally:
        # Shutdown: release connections
        engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/doentes/',
          status_code=HTTPStatus.CREATED,
          response_model=DoentePublic)
def create_doente(doente: DoenteSchema, db: Session = Depends(get_db)):
    # Pydantic v2 returns a date object if the schema uses `date`
    data = doente.model_dump()
    # Extra guard if tests send a string and schema wasn’t updated yet
    dn = data.get('data_nascimento')
    if isinstance(dn, str):
        data['data_nascimento'] = _date.fromisoformat(dn)

    obj = Doente(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

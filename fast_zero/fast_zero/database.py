from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# project root (where database.db will live)
BASE_DIR = Path(__file__).resolve().parents[1]
SQLALCHEMY_DATABASE_URL = f"sqlite:///{BASE_DIR / 'database.db'}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
     # needed for SQLite with FastAPI
    connect_args={"check_same_thread": False},
    future=True,
)

SessionLocal = sessionmaker(bind=engine,
                            autoflush=False,
                            autocommit=False,
                            future=True)
Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

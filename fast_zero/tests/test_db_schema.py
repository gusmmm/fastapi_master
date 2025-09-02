from sqlalchemy import inspect

from fast_zero.database import Base, engine


def test_doentes_table_is_created_and_exists():
    # Create all tables defined on metadata
    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert 'doentes' in tables

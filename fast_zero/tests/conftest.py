import pytest

from fast_zero.database import Base, engine


@pytest.fixture(autouse=True, scope="session")
def _create_schema():
    Base.metadata.create_all(bind=engine)
    # optionally: Base.metadata.drop_all(bind=engine)

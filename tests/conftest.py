import pytest

from faker import Faker

from app.dependencies import get_db_session

fake = Faker("en_US")


@pytest.fixture
def get_any_short_link() -> str:
    db_session = next(get_db_session())

    short_link = "gy"

    return short_link


@pytest.fixture
def create_long_link() -> dict:
    return {"url": fake.url()}

import json
import pytest
import random

from faker import Faker

from app.dependencies import get_db_session
from app.database import service

fake = Faker("en_US")


@pytest.fixture
def get_any_short_link() -> str:
    db_session = next(get_db_session())
    short_link = random.choice(service.get_all_short_links(db_session))

    return short_link


@pytest.fixture
def get_any_short_link_fake() -> str:
    return fake.uri()


@pytest.fixture
def create_long_link() -> dict:
    return json.dumps({"url": fake.url()})

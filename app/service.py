from app.database.models import LinkModel
from faker import Faker

fake = Faker()


def get_short_link(link_object: LinkModel) -> str:
    return fake.uri()

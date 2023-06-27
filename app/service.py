import string
from datetime import datetime

from app.database.models import LinkModel


def create_unique_id(link_id: int, created_at: datetime) -> int:
    return link_id + created_at.toordinal()


def create_short_url(unique_id: int) -> str:
    base62_string = string.ascii_letters + string.digits
    temp_url = ""

    while unique_id > 0:
        temp_url += base62_string[unique_id % 62]
        unique_id = unique_id // 62

    return temp_url


def get_short_link(link_object: LinkModel) -> str:
    unique_id = create_unique_id(link_id=link_object.id, created_at=link_object.created_at)
    short_url_reversed = create_short_url(unique_id=unique_id)

    return "".join(reversed(short_url_reversed))

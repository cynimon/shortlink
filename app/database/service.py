from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from app.database.models import LinkModel
from app.database.schemas import LongLinkSchema


def url_exists(db_session: Session, link_object: LongLinkSchema) -> bool:
    return bool(db_session.execute(select(LinkModel).where(LinkModel.long_link == link_object.url)).one_or_none())


def add_new_link(db_session: Session, link_object: LongLinkSchema) -> LinkModel:
    new_link_object = LinkModel(**{
        "long_link": link_object.url
    })
    db_session.add(new_link_object)
    db_session.commit()
    return new_link_object


def add_short_link(db_session: Session, short_link: str, link_object: LinkModel):
    link_object.short_link = short_link
    db_session.commit()


def get_long_link_by_short(db_session: Session, short_link: str) -> str:
    return db_session.scalars(select(LinkModel.long_link).where(LinkModel.short_link == short_link)).one()


def delete_link_by_short_url(db_session: Session, short_link: str):
    db_session.execute(delete(LinkModel).where(LinkModel.short_link == short_link))
    db_session.commit()

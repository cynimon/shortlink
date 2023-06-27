from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app import database
from app.config import get_config


settings = get_config()


def get_db_session() -> Session:
    session = database.SessionLocal()
    try:
        yield session
    finally:
        session.close()


DBSession = Annotated[Session, Depends(get_db_session)]

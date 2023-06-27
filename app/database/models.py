from sqlalchemy import Column, SmallInteger, String, DateTime, func

from app.database import Base


class LinkModel(Base):
    __tablename__ = 'link_table'

    id = Column(SmallInteger, primary_key=True)
    long_link = Column(String, unique=True, nullable=False)
    short_link = Column(String, unique=True, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f'LinkModel(id={self.id}, link={self.long_link})'

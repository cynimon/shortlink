from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import get_config

settings = get_config()

metadata = MetaData(naming_convention=settings.POSTGRES_INDEXES_NAMING_CONVENTION)

db_engine = create_engine(settings.database_url, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=db_engine, autoflush=False)
Base = declarative_base()

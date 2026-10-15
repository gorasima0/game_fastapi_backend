from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQL_URL = "sqlite:///./games.db"

engine = create_engine(
    SQL_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
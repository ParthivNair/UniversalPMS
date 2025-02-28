from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://cs340_nairp:7244@classmysql.engr.oregonstate.edu/cs340_nairp"

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=5
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
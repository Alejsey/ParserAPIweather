from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


"""url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="q1w2e3r4",  # plain (unescaped) text
    host="localhost",
    database="postgres",
)"""
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:q1w2e3r4@localhost:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)


Base = declarative_base()




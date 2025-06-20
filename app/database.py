"""
database.py
-----------
Central place that sets up the connection to PostgreSQL
and gives the rest of the app a session factory (SessionLocal)
plus a Base class for SQLAlchemy models to inherit from.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1) Read DATABASE_URL from the environment.
#    If you run the project with docker-compose it comes from
#    docker-compose.yml -> environment -> DATABASE_URL.
#    If you run locally without Docker, we fall back to localhost.
DB_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/customs",
)

# 2) Create an Engine – the core SQLAlchemy object that
#    holds the (lazy) connection-pool.
engine = create_engine(DB_URL, echo=False)

# 3) Each request gets its own short-lived database session.
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,   # we control commit/rollback manually
    autoflush=False     # safer; explicit flush on commit
)

# 4) Every ORM model class will inherit from this Base.
#    On startup we call Base.metadata.create_all() in app/main.py
#    to create tables if they don't exist.
Base = declarative_base()

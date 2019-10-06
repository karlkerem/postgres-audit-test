from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from postgresql_audit.flask import versioning_manager

# docker run --rm  --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/Projects/postgresql-audit-play/postgres:/var/lib/postgresql/data  postgres:11.5
engine = create_engine('postgresql://postgres:docker@localhost:5432/karl_test', echo=True)

Base = declarative_base()

versioning_manager.init(Base)

session = sessionmaker(bind=engine)()

# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python, SQLAlchemy e SQLite3.

``pip install sqlalchemy``.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class History(Base):
    __tablename__ = 'history'

    # Colunas da tabela.
    id = Column('id', Integer, primary_key=True)
    uri = Column('uri', String(1024))

    def __init__(self, uri=None):
        self.uri = uri


class Favorite(Base):
    __tablename__ = 'favorite'

    # Colunas da tabela.
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(1024))
    uri = Column('uri', String(1024))

    def __init__(self, title=None, uri=None):
        self.title = title
        self.uri = uri


# Base.metadata.drop_all(engine)
# History.__table__.create(engine)
# Favorite.__table__.create(engine)
Base.metadata.create_all(engine)

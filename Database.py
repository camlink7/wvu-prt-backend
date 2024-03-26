from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, String, Double
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import Session
import os

Base = declarative_base()
class Database():
    def __init__(self):

        engine = create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(
            os.getenv("DB_USER"), 
            os.getenv("DB_PASSWORD"), 
            os.getenv("DB_HOST"), 
            os.getenv("DB_NAME"))
        ,)

        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        session = scoped_session(DBSession)
        Base.query = session.query_property()

        self.session = session

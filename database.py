import re

import psycopg2
from sqlalchemy import (
    create_engine, Column, String, Integer
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

from change_dict import change_dict
import settings


db_url = 'postgresql://{username}:{password}@{host}/{db}'.format(
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    db=settings.DB_NAME
    )
engine = create_engine(db_url, echo=False)
Base = declarative_base()


def add_name_column():
    db_connection = psycopg2.connect(
        'host={} dbname={} user={} password={}'.format(
            settings.DB_HOST,
            settings.DB_NAME,
            settings.DB_USER,
            settings.DB_PASSWORD
            )
        )
    cur = db_connection.cursor()
    cur.execute('alter table streets add column name varchar(500);')
    db_connection.commit()
    cur.close()
    print('name column added successfully!')


class Street(Base):
    __tablename__ = 'streets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nm_tipo_lo = Column(String)
    nm_titulo_ = Column(String)
    nm_nome_lo = Column(String)
    wkb_geometry = Column(Geometry('MULTILINESTRING'))


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()


def fix_words(street_name, change_dict=change_dict):
    for key in change_dict:
        street_name = re.sub(r'\b%s\b' % key, change_dict[key], street_name)
    return street_name


def generate_name(tipo, titulo, nome):
    parts = [i.title() for i in [tipo, titulo, nome] if i is not None]
    name = ' '.join(parts)
    return fix_words(name)


def update_names():
    session = get_session()
    for street in session.query(Street).all():
        street.name = generate_name(
            street.nm_tipo_lo, street.nm_titulo_, street.nm_nome_lo
            )
    session.commit()

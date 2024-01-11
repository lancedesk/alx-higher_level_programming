#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City


def list_cities_states(username, password, db_name):
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_states = session.query(City).order_by(City.id).all()

    for city in cities_states:
        print(f'{city.id}: {city.name} -> {city.state.name}')


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    list_cities_states(sys.argv[1], sys.argv[2], sys.argv[3])

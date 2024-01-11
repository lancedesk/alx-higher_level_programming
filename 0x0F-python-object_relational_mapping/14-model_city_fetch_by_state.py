#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy.orm.exc import NoResultFound


def fetch_cities_by_state(username, password, db_name):
    """Fetches all City objects from the database sorted by cities.id."""
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all City objects and print the results
        cities = session.query(City, State).join(State).order_by(City.id).all()
        for city, state in cities:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
    except NoResultFound:
        pass
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to fetch City objects by state
    fetch_cities_by_state(username, password, db_name)

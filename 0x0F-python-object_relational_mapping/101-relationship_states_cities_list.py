#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states_and_cities(username, password, db_name):
    """List all State objects and their corresponding City objects."""
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb_name://{}:{}@localhost/{}'.
                           format(username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all State objects with their corresponding City objects
    states_cities = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(argv[0]))
        exit(1)

    # Get the command-line arguments
    username, password, db_name = argv[1], argv[2], argv[3]

    # Call the function to list states and cities
    list_states_and_cities(username, password, db_name)

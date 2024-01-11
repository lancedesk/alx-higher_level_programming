#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa (SQL injection free).
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state_by_name(username, password, db_name, state_name):
    """Prints the State object with the given name from the database."""
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State with the given name
    result = session.query(State).filter(State.name == state_name).first()

    # Display the result or "Not found" if no match
    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    username, password, db_name, state_name = (sys.argv[1],
                                               sys.argv[2],
                                               sys.argv[3],
                                               sys.argv[4])

    # Call the function to find the State by name
    find_state_by_name(username, password, db_name, state_name)

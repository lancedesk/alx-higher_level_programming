#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(username, password, db_name):
    """Changes the name of a State object in the database."""
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

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

    # Call the function to update the State object with id = 2
    update_state_name(username, password, db_name)

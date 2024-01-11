#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import warnings

# Suppress MySQL Connector/Python warning about MYSQL_OPT_RECONNECT deprecation
warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    module="mysql.connector.connection"
)


def add_louisiana(username, password, db_name):
    """Adds the State object "Louisiana" to the database and prints its id."""
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State object for Louisiana
    louisiana = State(name="Louisiana")

    # Add Louisiana to the session
    session.add(louisiana)

    # Commit the changes to the database
    session.commit()

    # Print the id of the newly added State object
    print(louisiana.id)

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

    # Call the function to add the State object "Louisiana"
    add_louisiana(username, password, db_name)

#!/usr/bin/python3
"""
Script that deletes the last two State objects with the name "Louisiana"
from the database hbtn_0e_6_usa.
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


def delete_last_two_louisiana(username, password, db_name):
    """Deletes the last two State objects with the name "Louisiana" from the database."""
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the last two Louisiana records
    louisiana_records = session.query(State).filter(State.name == "Louisiana").order_by(State.id.desc()).limit(2).all()

    # Delete the last two Louisiana records
    for record in louisiana_records:
        session.delete(record)

    # Commit the changes to the database
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

    # Call the function to delete the last two Louisiana records
    delete_last_two_louisiana(username, password, db_name)

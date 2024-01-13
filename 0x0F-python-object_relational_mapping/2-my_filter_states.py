#!/usr/bin/python3
"""
Filter and display values in the 'states' table
matching the provided state name.
Parameters:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database
    - state_name: Name of the state to filter and display
"""

import MySQLdb
import sys


def filter_states(username, password, db_name, state_name):
    """Display values in the states table matching the state name."""
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Format and execute the query to select states with the given name
    query = ("SELECT * FROM states WHERE name LIKE '{:s}' "
             "ORDER BY id ASC").format(state_name)
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


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

    # Call the function to filter states
    filter_states(username, password, db_name, state_name)

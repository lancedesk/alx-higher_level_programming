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


def safe_filter_states(username, password, db_name, state_name):
    """
    Display values in states table matching state name
    (safe from SQL injection).
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

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

    # Call the function to filter states (safe from SQL injection)
    safe_filter_states(username, password, db_name, state_name)

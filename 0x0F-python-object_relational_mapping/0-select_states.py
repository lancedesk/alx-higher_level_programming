#!/usr/bin/python3
"""
List all states from the 'states' table in a MySQL database.
Parameters:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database
"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """List all states from the database."""
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select states
    query = "SELECT * FROM states ORDER BY id ASC"
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
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, db_name)

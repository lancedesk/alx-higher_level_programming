#!/usr/bin/python3
import MySQLdb
import sys


def filter_cities_by_state(username, password, db_name, state_name):
    """List all cities of a state from database (safe from SQL injection)."""
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Use a parameterized query to avoid SQL injection
    query = (
             "SELECT GROUP_CONCAT(cities.name "
             "ORDER BY cities.id ASC SEPARATOR ', ') "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s"
            )
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Display the results
    if result:
        print(result)
    else:
        print("")

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

    # Call the function to filter cities by state
    filter_cities_by_state(username, password, db_name, state_name)

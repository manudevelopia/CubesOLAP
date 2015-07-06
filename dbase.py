"""Database Sevice ."""
import MySQLdb

from credentials import Credentials


class Dbase:

    """Dbase class manages Open, Query and Close database processes."""

    database = None
    cursor = None

    def open(self):
        """Establish a MySQL connection."""
        self.database = MySQLdb.connect(
            # MySQL database credentials
            Credentials.host,
            Credentials.user,
            Credentials.passwd,
            Credentials.db)

    def query(self, query, values):
        """Execute the MySQL Query."""
        # Get the cursor, which is used to traverse the database, line by line
        self.cursor = self.database.cursor()

        # Execute the query to persist the result
        self.cursor.execute(query, values)

        # Close the cursor
        self.cursor.close()

        # Commit the transaction
        self.database.commit()

    def close(self):
        """Close the database connection."""
        self.database.close()

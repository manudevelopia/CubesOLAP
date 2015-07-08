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
        # Get the cursor, which is used to traverse the database, line by line
        self.cursor = self.database.cursor()

    def query(self, query, values):
        """Execute the MySQL Query."""
        # Execute the query to persist the result
        self.cursor.execute(query, values)

        # Commit the transaction
        self.database.commit()

    def truncate(self, table):
        """Truncate the given table."""
        self.cursor.execute("TRUNCATE TABLE " + table)

    def close(self):
        """Close the cursor and database."""
        self.cursor.close()
        self.database.close()

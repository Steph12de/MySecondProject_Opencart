from utilities.readProperties import ReadConfig
import mysql.connector
from utilities.custom_logger import LogGen


class DatabaseHelpers:
    logger = LogGen.loggen()

    def __init__(self):
        # Step 1: Initialize connection attributes
        self.connection = None,
        self.cursor = None

    def connect_to_database(self):
        # Step 2: Establish database connection
        try:
            self.logger.info("Establishing database connection...")
            self.connection = mysql.connector.connect(
                host=ReadConfig.getHost(),
                port=ReadConfig.getPort(),
                user=ReadConfig.getUser(),
                password=ReadConfig.getDbPassword(),
                database=ReadConfig.getDatabase()
            )
            self.cursor = self.connection.cursor(buffered=True)
            self.logger.info("Database connection established")
        except mysql.connector.Error as e:
            self.logger.error(f"Database connection failed : {e} ")
            raise

    def read_from_database(self, query):
        # Step 3: Execute SELECT queries
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.logger.info(f"Query '{query}' executed successfully.")
            return result
        except mysql.connector.Error as e:
            self.logger.error(f"Query failed: {e}")
            raise

    def close_database_connection(self):
        # Step 4: Close cursor and connection
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            self.logger.info("Database connection closed.")
        except mysql.connector.Error as e:
            self.logger.error(f"Error while closing database connection: {e}")
            raise

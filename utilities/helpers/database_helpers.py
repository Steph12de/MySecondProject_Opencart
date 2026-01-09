from utilities.readProperties import ReadConfig
import mysql.connector
from utilities.custom_logger import LogGen


class DatabaseHelpers:
    logger = LogGen.loggen()

    def __init__(self):
        self.connection = None,
        self.cursor = None

    def connect_to_database(self):
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
            self.logger.error("Database connection failed : {e} ")
            raise

    def close_database_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        self.logger.info("Database connection closed.")

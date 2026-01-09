import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.getcwd(), "Configurations", "config.ini"))


class ReadConfig:
    @staticmethod
    def getEmail():
        email = config.get("common data", "email")
        return email

    @staticmethod
    def getPassword():
        password = config.get("common data", "password")
        return password

    @staticmethod
    def getNewPassword():
        new_password = config.get("common data", "new_password")
        return new_password

    @staticmethod
    def getWrongPassword():
        wrong_password = config.get("common data", "wrong_password")
        return wrong_password

    @staticmethod
    def getHost():
        host = config.get("database", "host")
        return host

    @staticmethod
    def getPort():
        port = config.get("database", "port")
        return port

    @staticmethod
    def getUser():
        user = config.get("database", "user")
        return user

    @staticmethod
    def getDbPassword():
        db_password = config.get("database", "db_password")
        return db_password

    @staticmethod
    def getDatabase():
        database = config.get("database", "database")
        return database

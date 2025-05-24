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
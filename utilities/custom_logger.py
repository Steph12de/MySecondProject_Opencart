import logging


class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        filehandler = logging.FileHandler(".\\Logs\\logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        return logger


import logging


class Logger:
    def __init__(self, log_file='app.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)

    @staticmethod
    def info(self, message):
        logging.info(message)

    @staticmethod
    def error(self, message):
        logging.error(message)
import logging


class Logger:
    def __init__(self, output_file):
        self.__output_file = output_file
        logging.basicConfig(filename=output_file, level=logging.DEBUG, format='%(asctime)s - %(levelname) - %(message)s')

    @property
    def output_file(self):
        return self.__output_file

    # Confirmation that things are working as expected.
    def info(self, message):
        logging.info(message)

    # An indication that something unexpected happened, or indicative of some problem in the near future
    # (e.g. ‘disk space low’). The software is still working as expected.
    def warning(self, message):
        logging.warning(message)

    # Detailed information, typically of interest only when diagnosing problems.
    def debug(self, message):
        logging.debug(message)

    # Due to a more serious problem, the software has not been able to perform some function.
    def error(self, message):
        logging.error(message)

    # A serious error, indicating that the program itself may be unable to continue running.
    def critical(self, message):
        logging.critical(message)

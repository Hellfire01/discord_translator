import logging


class Logger:
    def __init__(self, output_file):
        self.__output_file = output_file
        self.__logger = logging.getLogger(__name__)
        # prepare the file logging ( only has own log )
        file_handler = logging.FileHandler(self.__output_file)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)
        # prepare the stream handler ( competes with the other logs of the other used libs )
        stream_handler = logging.StreamHandler(self.__output_file)
        stream_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        self.__logger.addHandler(stream_handler)
        self.__logger.setLevel(logging.DEBUG)

    @property
    def output_file(self):
        return self.__output_file

    # Confirmation that things are working as expected.
    def info(self, log):
        self.__logger.info(log)

    # An indication that something unexpected happened, or indicative of some problem in the near future
    # (e.g. ‘disk space low’). The software is still working as expected.
    def warning(self, log):
        self.__logger.warning(log)

    # Detailed information, typically of interest only when diagnosing problems.
    def debug(self, log):
        self.__logger.debug(log)

    # Due to a more serious problem, the software has not been able to perform some function.
    def error(self, log):
        self.__logger.error(log)

    # A serious error, indicating that the program itself may be unable to continue running.
    def critical(self, log):
        self.__logger.critical(log)



class Core:
    def __init__(self):
        self.__database_interface = None
        self.__config = None

    @property
    def database_interface(self):
        return self.__database_interface

    @property
    def config(self):
        return self.__config

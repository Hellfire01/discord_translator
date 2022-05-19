

class DatabaseConfig:
    def __init__(self, database_interface):
        self.__database_interface = database_interface

    @property
    def database_interface(self):
        return self.__database_interface

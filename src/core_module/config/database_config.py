

class DatabaseConfig:
    def __init__(self, database_name):
        self.__database_name = database_name

    @property
    def database_name(self):
        return self.__database_name

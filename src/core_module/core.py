

class Core:
    def __init__(self, commandline_config, database_config, discord_config, translate_config, logger, database_access):
        self.__commandline_config = commandline_config
        self.__database_config = database_config
        self.__discord_config = discord_config
        self.__translate_config = translate_config
        self.__logger = logger
        self.__database_access = database_access

    @property
    def commandline_config(self):
        return self.__commandline_config

    @property
    def database_config(self):
        return self.__database_config

    @property
    def discord_config(self):
        return self.__discord_config

    @property
    def translate_config(self):
        return self.__translate_config

    @property
    def logger(self):
        return self.__logger

    @property
    def database_access(self):
        return self.__database_access



class Core:
    def __init__(self, command_line_config, database_config, discord_config, translate_config):
        self.__command_line_config = command_line_config
        self.__database_config = database_config
        self.__discord_config = discord_config
        self.__translate_config = translate_config

    @property
    def command_line_config(self):
        return self.__command_line_config

    @property
    def database_config(self):
        return self.__database_config

    @property
    def discord_config(self):
        return self.__discord_config

    @property
    def translate_config(self):
        return self.__translate_config

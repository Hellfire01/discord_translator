

class DiscordConfig:
    def __init__(self, token):
        self.__discord_token = token

    @property
    def discord_token(self):
        return self.__discord_token

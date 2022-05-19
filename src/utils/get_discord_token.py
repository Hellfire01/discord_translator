import os
from pathlib import Path


class GetDiscordToken:
    @staticmethod
    def get_discord_token(filename) -> str:
        file_path = Path(os.getcwd()) / filename
        try:
            with open(file_path) as file:
                token = file.readline()
        except FileNotFoundError:
            print("could not find the needed token file " + str(file_path))
            exit(1)
        return token

import os
from pathlib import Path


class GlobalSettings:
    __instance = None

    def __init__(self):
        self.instruction_keyword = None
        self.discord_token = None
        self.translate_splitter = None

    def __get_discord_token(self, filename) -> str:
        file_path = Path(os.getcwd()) / filename
        try:
            with open(file_path) as file:
                token = file.readline()
        except FileNotFoundError:
            print("could not find the needed token file " + str(file_path))
            exit(1)
        return token

    def set_values(self, instruction_keyword, discord_token_filename, translate_splitter):
        self.instruction_keyword = instruction_keyword
        self.discord_token = self.__get_discord_token(discord_token_filename)
        self.translate_splitter = translate_splitter

    @staticmethod
    def get_instance():
        if GlobalSettings.__instance is None:
            GlobalSettings.__instance = GlobalSettings()
        return GlobalSettings.__instance

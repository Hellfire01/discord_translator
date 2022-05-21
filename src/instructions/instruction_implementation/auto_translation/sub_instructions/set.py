from src.instructions.enums.lang_enum import LangEnum
from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Set(InstructionParent):
    def __init__(self, commandline_config):
        self.commandline_config = commandline_config
        super(Set, self).__init__("Auto translation Set")

    def __get_lang(self, string):
        langs = [e.value for e in LangEnum]
        langs.remove(LangEnum.NOT_A_LANG.value)
        for lang in langs:
            if string == lang.name or string == lang.acronym or string in lang.emotes:
                return lang
        return LangEnum.NOT_A_LANG

    def run(self, message):
        split_message = message.strip().split(" ")[1:]
        if len(split_message) == 0:
            return "This instruction requires at least one language given as parameter"
        langs = set()
        for lang_string in split_message:
            lang = self.__get_lang(lang_string)
            if lang is LangEnum.NOT_A_LANG:
                ret = "'" + lang_string + "' is not recognised as a valid language\n"
                ret += "to have the list of valid languages use : `" + self.commandline_config.first_keyword + " lang-list`"
                return ret
            langs.add(lang)
        # is channel already in database ?
        # if yes overwrite existing auto translation and say so
        # if no, set auto translation and recap instruction
        return "Auto translation set todo"

    def get_description(self) -> str:
        ret = "The set instruction tells the translator that you would like the current channel to be auto translated\n"
        ret += "In order to use it, give one or more languages as parameter\n"
        ret += "Example : `!ot auto-translate set fr en` sets the current channel to auto translate all messages to" \
               "french and english"
        return ret

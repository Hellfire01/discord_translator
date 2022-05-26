from src.instructions.enums.lang_enum import LangEnum
from src.instructions.instruction_implementation.auto_translation.common.lang_instruction import LangInstruction
from src.instructions.instruction_implementation.auto_translation.common.get_permission import GetPermission
from src.instructions.instruction_inheritance import InstructionParent


class Set(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.database_access = database_access
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
        if GetPermission.check_if_allowed(message) is False:
            ret = "I apologise it seams you do not have the required permissions in order to change the auto translation settings\n"
            ret += "By default only the owner of the discord guild can change this setting\n"
            ret += "The owner of the discord guild can add allowed roles using the `" + self.commandline_config.first_keyword + " trusted-roles` instruction\n"
            return ret
        split_message = message.content.strip().split(" ")[3:]
        if len(split_message) == 0:
            return "This instruction requires at least one language given as parameter"
        langs = []
        for lang_string in split_message:
            lang = self.__get_lang(lang_string)
            if lang is LangEnum.NOT_A_LANG:
                ret = "'" + lang_string + "' is not recognised as a valid language\n"
                ret += "to have the list of valid languages use : `" + self.commandline_config.first_keyword + " lang-list`"
                return ret
            if lang not in langs:
                langs.append(lang)
        lang_str = LangInstruction.get_instruction_from_langs(langs)
        self.database_access.set_channel_instruction(message.channel.id, lang_str)
        return "setting current channel auto translation to : " + lang_str

    def get_description(self) -> str:
        ret = "The set instruction tells the translator that you would like the current channel to be auto translated\n"
        ret += "In order to use it, give one or more languages as parameter\n"
        ret += "Example : `!ot auto-translate set fr en` sets the current channel to auto translate all messages to" \
               "french and english"
        return ret

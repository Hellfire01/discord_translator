from src.logger.logger import Logger
from src.instructions.enums.lang_enum import LangEnum


class LangInstruction:
    separator = " / "

    @staticmethod
    def __get_lang(string, possible_langs):
        for lang in possible_langs:
            # the database only stores the complete name, the acronyms and emotes are left for future proofing
            if string == lang.name or string == lang.acronym or string in lang.emotes:
                return lang
        return LangEnum.NOT_A_LANG

    @staticmethod
    def get_langs_from_instruction(logger, channel_id, instruction):
        split = instruction.split(LangInstruction.separator)
        possible_langs = [e.value for e in LangEnum]
        possible_langs.remove(LangEnum.NOT_A_LANG.value)
        langs = []
        for given_lang in split:
            buffer = LangInstruction.__get_lang(given_lang, possible_langs)
            if buffer is LangEnum.NOT_A_LANG:
                logger.warning("found unmanaged lang '" + given_lang + "' for channel " + str(channel_id))
            else:
                langs.append(buffer)
        return langs

    @staticmethod
    def get_instruction_from_langs(langs) -> str:
        return LangInstruction.separator.join([e.name for e in langs])

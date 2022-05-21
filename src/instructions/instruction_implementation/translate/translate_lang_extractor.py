from src.exceptions.translate_exception import TranslateException
from src.instructions.enums.lang_enum import LangEnum


class TranslateLangExtractor:
    def __init__(self, translate_config, translate_help_instruction, translate_lang_list_instruction):
        self.translate_config = translate_config
        self.translate_help_instruction = "Use " + translate_help_instruction + " for help / to see examples"
        self.translate_lang_list_instruction = "Use " + translate_lang_list_instruction + " to see the available languages"

    def __check_for_separator(self, message):
        s_message = message.content.split(self.translate_config.separator)
        if len(s_message) < 2:
            err = "I could not find the separator `" + self.translate_config.separator + "`"
            err += " that I need to know what to translate into what.\n"
            err += self.translate_help_instruction
            raise TranslateException(err)
        return s_message

    def __check_for_instructions_text_separation(self, split_message):
        if len(split_message) < 2:
            if len(split_message[0]) > 20:
                message = "I need a carriage return / line break ( the ENTER key ) to allow me to separate the languages "
                message += "from the text you would like me to translate\n"
            else:
                message = "I need to have text to translate with this instruction\n"
                message += "What would you like me to translate ?\n"
            message += self.translate_help_instruction
            raise TranslateException(message)

    def __check_no_multiple_input_langs(self, message_input_instructions):
        split_message = message_input_instructions.strip().split(" ")
        if len(split_message) > 1:
            message = "I cannot have more than one input language ( I was given " + ", ".join(split_message) + " )\n"
            message += self.translate_help_instruction
            raise TranslateException(message)

    def __get_lang(self, string):
        langs = [e.value for e in LangEnum]
        langs.remove(LangEnum.NOT_A_LANG.value)
        for lang in langs:
            if string == lang.name or string == lang.acronym or string in lang.emotes:
                return lang
        return LangEnum.NOT_A_LANG

    def __raise_unrecognised_lang_error(self, string, input_output):
        message = "I can not use " + string + " as an " + input_output + " language\n"
        message += self.translate_lang_list_instruction + "\n"
        message += self.translate_help_instruction
        raise TranslateException(message)

    def __get_input_lang(self, message_input_instructions):
        message_input_instructions_stripped = message_input_instructions.strip()
        if message_input_instructions_stripped == "":
            return LangEnum.NOT_A_LANG
        self.__check_no_multiple_input_langs(message_input_instructions_stripped)
        lang = self.__get_lang(message_input_instructions_stripped)
        if lang is LangEnum.NOT_A_LANG:
            self.__raise_unrecognised_lang_error(message_input_instructions_stripped, "input")
        else:
            return lang

    def __get_output_lang(self, message_output_instructions):
        given_langs = message_output_instructions.strip().split(" ")
        if len(given_langs) == 0:
            message = "I did not find any languages to translate to, I need output languages in order to be able"
            message += " to translate\n"
            message += self.translate_help_instruction
            raise TranslateException(message)
        else:
            langs = []
            for given_lang in given_langs:
                buffer = self.__get_lang(given_lang)
                if buffer is LangEnum.NOT_A_LANG:
                    self.__raise_unrecognised_lang_error(given_lang, "output")
                else:
                    langs.append(buffer)
        return langs

    def get_langs(self, message):
        split_message = message.split("\n")
        message_instruction_list = self.__check_for_separator(split_message[0])
        self.__check_for_instructions_text_separation(split_message)
        input_lang = self.__get_input_lang(message_instruction_list[0])
        output_langs = self.__get_output_lang(message_instruction_list[1])
        output_langs = list(dict.fromkeys(output_langs))  # remove duplicates
        return input_lang, output_langs

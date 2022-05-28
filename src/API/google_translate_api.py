from src.instructions.enums.lang_enum import LangEnum
from functools import cache
from googletrans import Translator
import time


class GoogleTranslateApi:
    def __init__(self, api_config):
        self.translator = Translator()
        self.api_config = api_config

    @cache
    def __translate(self, message_string, input_lang, output_lang) -> str:
        if input_lang is not LangEnum.NOT_A_LANG and input_lang is not None:
            buffer = self.translator.translate(message_string, src=input_lang.acronym, dest=output_lang.acronym)
        else:
            buffer = self.translator.translate(message_string, dest=output_lang.acronym)
        time.sleep(self.api_config.api_sleep)
        return buffer.text

    def translate(self, message_string, input_lang, output_lang) -> str:
        if len(message_string) > self.api_config.max_message_len:
            return self.__translate(self.api_config.max_len_error_message, None, output_lang)
        return self.__translate(message_string, input_lang, output_lang)

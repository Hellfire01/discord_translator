from src.instructions.enums.lang_enum import LangEnum
from functools import cache
from googletrans import Translator
import time


class GoogleTranslateApi:
    def __init__(self, api_config):
        self.translator = Translator()
        self.api_config = api_config

    @cache
    def translate(self, message_string, input_lang, output_lang) -> str:
        if input_lang is not LangEnum.NOT_A_LANG and input_lang is not None:
            buffer = self.translator.translate(message_string, src=input_lang.acronym, dest=output_lang.acronym)
        else:
            buffer = self.translator.translate(message_string, dest=output_lang.acronym)
        time.sleep(self.api_config.__google_api_sleep)
        return buffer.text

from src.instructions.enums.lang_enum import LangEnum
from googletrans import Translator


class GoogleTranslateApi:
    def __init__(self):
        self.translator = Translator()

    def translate(self, message, input_lang, output_lang) -> str:
        if input_lang is not LangEnum.NOT_A_LANG:
            buffer = self.translator.translate(message, src=input_lang.acronym, dest=output_lang.acronym)
            return buffer.text
        else:
            buffer = self.translator.translate(message, dest=output_lang.acronym)
            return buffer.text
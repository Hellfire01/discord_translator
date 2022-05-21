from src.instructions.enums.lang_enum import LangEnum
from src.instructions.instruction_implementation.instruction_parent import InstructionParent
from src.instructions.instruction_implementation.translate.translate_lang_extractor import TranslateLangExtractor
from src.API.google_translate_api import GoogleTranslateApi
from src.exceptions.translate_exception import TranslateException


class TranslateSubInstruction(InstructionParent):
    def __init__(self, commandline_config, translate_config, translate_help_instruction, translate_lang_list_instruction):
        self.commandline_config = commandline_config
        self.translate_config = translate_config
        self.extractor = TranslateLangExtractor(translate_config, translate_help_instruction, translate_lang_list_instruction)
        self.translate_lang_list_instruction = translate_lang_list_instruction
        self.translate_help_instruction = translate_help_instruction
        self.googleTranslateApi = GoogleTranslateApi()
        super(TranslateSubInstruction, self).__init__("Translate Instruction")

    def run(self, message_string) -> str:
        try:
            input_lang, output_langs = self.extractor.get_langs(" ".join(message_string.strip().split(" ")))
            ret = "requested input lang is "
            if input_lang == LangEnum.NOT_A_LANG:
                ret += "to be automatically detected\n"
            else:
                ret += input_lang.name + " \n"
            ret += "requested output langs are : "
            join = False
            for output_lang in output_langs:
                if join is False:
                    join = True
                else:
                    ret += ", "
                ret += output_lang.name
            ret += "\n"
            to_translate = "\n".join(message_string.split("\n")[1:])
            for output_lang in output_langs:
                ret += "\n" + output_lang.emotes[0] + " " + self.googleTranslateApi.translate(to_translate, input_lang, output_lang)
        except TranslateException as e:
            return str(e)
        return ret

    def get_description(self):
        return "use `" + self.commandline_config.first_keyword + " translate help` in order to know " \
               "how to use this instruction"

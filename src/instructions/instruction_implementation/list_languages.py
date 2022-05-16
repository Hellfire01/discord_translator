from src.instructions.enums.lang_enum import LangEnum
from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class ListLanguages(InstructionParent):
    def __init__(self):
        super(ListLanguages, self).__init__("Languages list")

    def run(self, message) -> str:
        ret = "Here is a list of all of the languages I am able to translate :\n\n"
        langs = [e.value for e in LangEnum]
        langs.remove(LangEnum.NOT_A_LANG.value)
        langs.sort()
        for lang in langs:
            ret += "`" + lang.name + "` " + lang.acronym + " => "
            for flag in lang.emotes:
                ret += flag + " "
            ret += "\n"
        return ret

    def get_description(self) -> str:
        return "presents all of the available languages of the translator and the associated emotes"

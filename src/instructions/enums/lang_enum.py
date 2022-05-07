from src.instructions.enums.lang import Lang
from enum import Enum


class LangEnum(Enum):
    NOT_A_LANG = None
    ENGLISH = Lang([":flag_us:", ":flag_gb:"], "english", "en")
    FRENCH = Lang([":flag_fr:"], "french", "fr")
    ITALIAN = Lang([":flag_it:"], "italian", "it")
    GERMAN = Lang([":flag_de:"], "german", "de")
    RUSSIAN = Lang([":flag_ru:"], "russian", "ru")
    SPANISH = Lang([":flag_es:"], "spanish", "es")
    UKRAINIAN = Lang([":flag_ua:"], "ukrainian", "uk")

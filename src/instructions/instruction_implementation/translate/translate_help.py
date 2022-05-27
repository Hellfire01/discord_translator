from src.instructions.instruction_inheritance import InstructionParent


class TranslateHelp(InstructionParent):
    def __init__(self, commandline_config, translate_config):
        self.commandline_config = commandline_config
        self.translate_config = translate_config
        super(TranslateHelp, self).__init__("Translate Help")

    def run(self, message):
        ret = "This is the `translate` option\n"
        ret += "The translation is made using google translate\n"
        ret += "The option is used for a direct translation between a given text and the expected output\n"
        ret += "To use it, use the flag emotes, names or acronyms. The available flag emotes can be listed with the `" + \
               self.commandline_config.first_keyword + " lang-list` instruction\n"
        ret += "The first flag is for the input languages, the following ones are the output languages\n"
        ret += "\n"
        ret += "Usage example :\n"
        ret += "**" + self.commandline_config.first_keyword + " translate en " + self.translate_config.separator + " french**\n"
        ret += "This will attempt to take in english and translate it automatically to french\n"
        ret += "\n"
        ret += "Usage example :\n"
        ret += "**" + self.commandline_config.first_keyword + " translate " + self.translate_config.separator + " it**\n"
        ret += "The translator will attempt to guess the input language and output it to italian\n"
        ret += "This may have mixed results if the input language is not correctly guessed though\n"
        return ret

    def get_description(self) -> str:
        return "this instruction_implementation shows you how to use the `translate` option"

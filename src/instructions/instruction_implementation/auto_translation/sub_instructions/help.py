from src.instructions.instruction_inheritance import InstructionParent


class Help(InstructionParent):
    def __init__(self, commandline_config):
        self.commandline_config = commandline_config
        super(Help, self).__init__("Auto translation Help")

    def run(self, message):
        ret = "This is the `auto-translation` instruction\n"
        ret += "\n"
        ret += "This is where you configure a channel ( the current one ) in order to have a fully automated translation\n"
        ret += "The understood instructions are as follow :\n"
        ret += "\n"
        ret += "`" + self.commandline_config.first_keyword + " auto-translation set [langs]` sets the current channel to be automatically translated\n"
        ret += "the **[langs]** needs to be replaced with the languages you wish to see auto translated\n"
        ret += "you can get the language list by using the `" + self.commandline_config.first_keyword + " lang-list` instruction\n"
        ret += "usage example : `" + self.commandline_config.first_keyword + " auto-translation set fr en` for a french / english auto translation\n"
        ret += "\n"
        ret += "`" + self.commandline_config.first_keyword + " auto-translation get` displays the auto translate instruction for the current channel\n"
        ret += "\n"
        ret += "`" + self.commandline_config.first_keyword + " auto-translation remove` removes the auto translation from the current channel\n"
        return ret

    def get_description(self) -> str:
        return "this instruction implementation shows you how to use the `auto-translation` option"

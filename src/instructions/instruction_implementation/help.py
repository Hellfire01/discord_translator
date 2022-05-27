from src.instructions.instruction_inheritance import InstructionParent


class Help(InstructionParent):
    def __init__(self, keyword):
        self.keyword = keyword
        super(Help, self).__init__("Help")

    def run(self, message=None) -> str:
        ret = "Hello :wave:\n"
        ret += "I am a translator, I automate the usage of google translate in order to allow different " \
               "communities to easily interact with one another\n"
        ret += "I can manage multiple different languages as input and output\n"
        ret += "\n"
        ret += "Here is how to use me :\n"
        ret += "\n"
        ret += "I can be set to translate a text channel automatically in the desired languages by using the " \
               "`auto-translation` instruction\n"
        ret += "By default, only the  server owner can use this instruction, in order to add roles that are " \
               "allowed to setup / change / remove the auto translated channels, you can use the `trusted-roles`" \
               " instruction ( server owner only )\n"
        ret += "\n"
        ret += "you can get the complete list of instructions I understand by writing : `" + self.keyword + " list`\n"
        return ret

    def get_description(self):
        return "this instruction allows you to know how to set up and use the bot"

from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Help(InstructionParent):
    def __init__(self, keyword):
        self.keyword = keyword
        super(Help, self).__init__("Help")

    def run(self, message=None) -> str:
        ret = "Hello :wave:\n"
        ret += "I am a translator, I get the messages that are given to me and send them to google translate\n"
        ret += "I can manage multiple different languages as output\n"
        ret += "My goal is to help people of different communities and languages communicate with each other\n"
        ret += "\n"
        ret += "Here is how to use me :\n"
        ret += "\n"
        ret += "you can get the list of instruction_implementation by writing `" + self.keyword + " -l`"
        return ret

    def get_description(self):
        return "this instruction allows you to know how to set up and use the bot"

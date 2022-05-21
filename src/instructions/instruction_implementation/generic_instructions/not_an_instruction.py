from src.instructions.instruction_inheritance import InstructionParent


class NotAnInstruction(InstructionParent):
    def __init__(self, commandline_config, extra_message=""):
        self.extra_message = extra_message
        self.commandline_config = commandline_config
        super(NotAnInstruction, self).__init__("// not an instruction")

    def run(self, message) -> str:
        ret = ""
        if message.content.strip() == self.commandline_config.first_keyword:
            ret = "you need to give me an instruction if you want me to do something\n"
        else:
            ret += "I'm sorry I could not understand this instruction :cry:\n"
        if self.extra_message != "":
            ret += self.extra_message + "\n"
        else:
            ret += "use `" + self.commandline_config.first_keyword + " --help`"
        return ret

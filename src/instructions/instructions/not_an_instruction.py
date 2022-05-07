from src.instructions.instructions.instruction_parent import InstructionParent
from src.global_settings import GlobalSettings


class NotAnInstruction(InstructionParent):
    def __init__(self, extra_message=""):
        super(NotAnInstruction, self).__init__("// not an instruction")
        self.extra_message = extra_message

    def run(self, message) -> str:
        ret = ""
        if message.strip() == GlobalSettings.get_instance().instruction_keyword:
            ret = "you need to give me an instruction if you want me to do something\n"
        else:
            ret += "I'm sorry I could not understand this instruction :cry:\n"
        if self.extra_message != "":
            ret += self.extra_message + "\n"
        else:
            ret += "use `" + GlobalSettings.get_instance().instruction_keyword[0] + " --help`"
        return ret

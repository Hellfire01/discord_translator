from src.instructions.instruction_inheritance import InstructionParent


class Help(InstructionParent):
    def __init__(self):
        super(Help, self).__init__("Auto translation Help")

    def run(self, message):
        ret = "This is the `auto-translation` option\n"
        ret += "This is where you configure a channel ( the current one ) in order to have a fully automated translation\n"
        return ret

    def get_description(self) -> str:
        return "this instruction_implementation shows you how to use the `auto-translation` option"

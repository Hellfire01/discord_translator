from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Remove(InstructionParent):
    def __init__(self):
        super(Remove, self).__init__("Auto translation Remove")

    def run(self, message):
        return "Auto translation remove todo"

    def get_description(self) -> str:
        ret = "This instruction will remove this channel from the list of managed channels.\n"
        ret += "This removes the auto translation for this channel"
        return ret

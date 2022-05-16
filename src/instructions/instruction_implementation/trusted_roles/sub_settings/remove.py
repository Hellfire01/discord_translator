from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Remove(InstructionParent):
    def __init__(self):
        super(Remove, self).__init__("Channel settings remove")

    def run(self, message):
        return "trusted roles remove todo"

    def get_description(self) -> str:
        return "trusted roles remove description todo"

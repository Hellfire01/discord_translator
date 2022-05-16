from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Remove(InstructionParent):
    def __init__(self):
        super(Remove, self).__init__("Channel settings remove")

    def run(self, message):
        return "user preferences remove todo"

    def get_description(self) -> str:
        return "user preferences remove description todo"

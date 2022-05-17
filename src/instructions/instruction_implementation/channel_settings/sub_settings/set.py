from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Set(InstructionParent):
    def __init__(self):
        super(Set, self).__init__("Channel settings Set")

    def run(self, message):
        return "channel settings set todo"

    def get_description(self) -> str:
        return "channel settings set description todo"

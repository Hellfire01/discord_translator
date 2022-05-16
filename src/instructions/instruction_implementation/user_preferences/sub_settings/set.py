from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Set(InstructionParent):
    def __init__(self):
        super(Set, self).__init__("Channel settings set")

    def run(self, message):
        return "user preferences set todo"

    def get_description(self) -> str:
        return "user preferences set description todo"

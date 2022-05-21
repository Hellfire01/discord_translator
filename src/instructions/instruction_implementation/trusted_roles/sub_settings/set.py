from src.instructions.instruction_inheritance import InstructionParent


class Set(InstructionParent):
    def __init__(self):
        super(Set, self).__init__("Channel settings set")

    def run(self, message):
        return "trusted roles set todo"

    def get_description(self) -> str:
        return "trusted roles set description todo"

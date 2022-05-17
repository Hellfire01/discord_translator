from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Set(InstructionParent):
    def __init__(self):
        super(Set, self).__init__("Auto translation Set")

    def run(self, message):
        return "Auto translation set todo"

    def get_description(self) -> str:
        return "Auto translation set description todo"

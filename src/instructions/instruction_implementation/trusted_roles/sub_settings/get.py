from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Get(InstructionParent):
    def __init__(self):
        super(Get, self).__init__("Channel settings get")

    def run(self, message):
        return "trusted roles get todo"

    def get_description(self) -> str:
        return "trusted roles get description todo"

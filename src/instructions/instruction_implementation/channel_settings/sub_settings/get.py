from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Get(InstructionParent):
    def __init__(self):
        super(Get, self).__init__("Channel settings Get")

    def run(self, message):
        return "channel settings get todo"

    def get_description(self) -> str:
        return "channel settings get description todo"

from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Get(InstructionParent):
    def __init__(self):
        super(Get, self).__init__("Auto translation Get")

    def run(self, message):
        return "Auto translation get todo"

    def get_description(self) -> str:
        return "This instruction will display the settings being applied in the current channel"

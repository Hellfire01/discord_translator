from src.instructions.instructions.instruction_parent import InstructionParent


class NoInstruction(InstructionParent):
    def __init__(self):
        super(NoInstruction, self).__init__("// no instruction")

    def run(self, message) -> str:
        return ""

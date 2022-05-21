

class AutomatedInstructionParent:
    def __init__(self, instruction_name):
        self.instruction_name = instruction_name

    def run(self, message) -> str:
        return "the instruction was not properly overloaded"

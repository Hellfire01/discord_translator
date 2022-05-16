from src.instructions.instruction_implementation.help import Help
from src.instructions.instruction_implementation.not_an_instruction import NotAnInstruction
from src.instructions.instruction_implementation.no_instruction import NoInstruction


# dataclass that references the complete list of all the instruction_implementation
class InstructionReferencer:
    def __init__(self, help_instruction=None, no_instruction=None, not_an_instruction=None, default_instruction=None):
        self.no_instruction = NoInstruction() if no_instruction is None else no_instruction
        self.not_an_instruction = NotAnInstruction() if not_an_instruction is None else not_an_instruction
        self.help_instruction = Help() if help_instruction is not None else help_instruction
        self.default_instruction = default_instruction
        self.instructions = [
        ]
        # gets called on all messages if not an instruction
        self.automated_instructions = [
        ]

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def add_automated_instruction(self, automated_instruction):
        self.automated_instructions.append(automated_instruction)

    def get_instruction_list(self) -> tuple:
        return self.instructions, self.automated_instructions

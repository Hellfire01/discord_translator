from src.instructions.instructions.instruction_parent import InstructionParent


class InstructionExtractor:
    def __init__(self, keywords, instruction_referencer):
        self.instruction_keywords = keywords
        self.instructions_references = instruction_referencer

    def is_instruction(self, message):
        if len(self.instruction_keywords) == 0:
            return True
        for keyword in self.instruction_keywords:
            if message.startswith(keyword):
                return True
        return False

    @property
    def help_instruction(self):
        return self.instructions_references.help_instruction

    def get_instruction(self, message: str) -> InstructionParent:
        clear_message = message.strip()
        if self.is_instruction(message):
            split_message = clear_message.split(' ')
            if len(split_message) < 2:
                return self.instructions_references.not_an_instruction
            for instruction in self.instructions_references.instructions:
                for keyword in instruction.keywords:
                    if split_message[1] == keyword:
                        return instruction.reference
            return self.instructions_references.not_an_instruction
        else:
            for instruction in self.instructions_references.automated_instructions:
                for keyword in instruction.keywords:
                    if clear_message == keyword:
                        return instruction.reference
            return self.instructions_references.no_instruction


# create a sub parser for the sub instruction menus
# the parser needs to send the message with the instruction keyword + instruction command removed
# instructions todo :
#   channel
#     check ( status of current channel )
#     list ( on this discord )
#     set
#     unset
#   user ( on himself ) / channel dependant
#     check
#     set
#     unset


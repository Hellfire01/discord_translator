

class SubInstructionExtractor:
    def __init__(self, keywords, instruction_referencer):
        self.instruction_keywords = keywords
        self.instructions_references = instruction_referencer

    @property
    def help_instruction(self):
        return self.instructions_references.help_instruction

    def get_instruction(self, message_string):
        clear_message = message_string.strip()
        split_message = clear_message.split(' ')
        if len(split_message) == 0 or len(split_message) == 1 and split_message[0] == "":
            return self.instructions_references.not_an_instruction
        for instruction in self.instructions_references.instructions:
            for keyword in instruction.keywords:
                if split_message[0] == keyword:
                    return instruction.reference
        if self.instructions_references.default_instruction is not None:
            return self.instructions_references.default_instruction
        return self.instructions_references.not_an_instruction

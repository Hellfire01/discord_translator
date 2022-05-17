from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class InstructionList(InstructionParent):
    def __init__(self, get_instruction_list, sub_instruction_string=""):
        self.get_instruction_list = get_instruction_list
        self.sub_instruction_string = sub_instruction_string
        super(InstructionList, self).__init__(sub_instruction_string + "Instruction list")

    def __present_keywords(self, keywords) -> str:
        ret = ""
        index = 0
        while index < len(keywords):
            ret += '`' + keywords[index] + '`'
            if index < len(keywords) - 2:
                ret += ", "
            elif index < len(keywords) - 1:
                ret += " or "
            index += 1
        return ret

    def run(self, message) -> str:
        ret = ""
        instructions, nk_instructions = self.get_instruction_list()
        ret += "list of possible instructions :\n"
        instructions.sort()
        for instruction in instructions:
            ret += "\n"
            ret += "**" + instruction.reference.instruction_name + "** => can be called with :"
            ret += " " + self.__present_keywords(instruction.keywords) + "\n"
            ret += instruction.reference.get_description() + "\n"
        for nk_instruction in nk_instructions:
            pass
        return ret

    def get_description(self):
        return "displays a complete list of all of the available instruction_implementation and how to use them"

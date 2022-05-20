from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Set(InstructionParent):
    def __init__(self):
        super(Set, self).__init__("Auto translation Set")

    def run(self, message):
        split_message = message.strip().split(" ")[1:]
        if len(split_message) == 0:
            return "This instruction requires at least one language given as parameter"
        # are given parameter languages ?
        # remove language duplicates
        # is channel already in database ?
        # if yes overwrite existing auto translation and say so
        # if no, set auto translation and recap instruction
        return "Auto translation set todo"

    def get_description(self) -> str:
        ret = "The set instruction tells the translator that you would like the current channel to be auto translated\n"
        ret += "In order to use it, give one or more languages as parameter\n"
        ret += "Example : `!ot auto-translate set fr en` sets the current channel to auto translate all messages to" \
               "french and english"
        return ret

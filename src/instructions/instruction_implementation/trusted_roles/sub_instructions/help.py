from src.instructions.instruction_inheritance import InstructionParent


class Help(InstructionParent):
    def __init__(self):
        super(Help, self).__init__("Trusted Roles Help")

    def run(self, message):
        ret = "This is the `trusted-roles` option\n"
        ret += "This instruction allows you to set who is allowed to change the auto translation settings for your channels\n"
        ret += "By default there are no roles configured and only the server owner can setup the auto translations"
        return ret

    def get_description(self) -> str:
        return "this instruction implementation shows you how to use the `trusted-roles` option"

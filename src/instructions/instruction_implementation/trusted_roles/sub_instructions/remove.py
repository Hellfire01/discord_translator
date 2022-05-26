from src.instructions.instruction_implementation.comon.get_permission import GetPermission
from src.instructions.instruction_inheritance import InstructionParent


class Remove(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Remove, self).__init__("Trusted roles remove")

    def run(self, message):
        if GetPermission.check_if_owner(message) is False:
            ret = "I apologise but only the discord guild owner may use this instruction\n"
            ret += "The owner of the discord guild can add allowed roles using the `" + self.commandline_config.first_keyword + " trusted-roles` instruction\n"
            return ret
        return ""

    def get_description(self) -> str:
        return "trusted roles remove description todo"

from src.instructions.instruction_implementation.comon.get_permission import GetPermission
from src.instructions.instruction_inheritance import InstructionParent


class Get(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Get, self).__init__("Trusted roles get")

    def run(self, message):
        if GetPermission.check_if_owner(message) is False:
            ret = "I apologise but only the discord guild owner may use this instruction\n"
            ret += "The owner of the discord guild can add allowed roles using the `" + self.commandline_config.first_keyword + " trusted-roles` instruction\n"
            return ret
        roles = self.database_access.get_trusted_roles(message.guild.id)
        if len(roles) == 0:
            return "There are currently no roles allowed to edit the auto translate settings on this discord guild\n"
        ret = "The roles that can edit this discord's guild auto translation settings are : \n"
        ret += "\n".join(role.role_name for role in roles)
        return ret

    def get_description(self) -> str:
        return "trusted roles get description todo"

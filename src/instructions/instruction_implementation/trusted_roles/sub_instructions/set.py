from src.instructions.instruction_implementation.comon.get_permission import GetPermission
from src.instructions.instruction_inheritance import InstructionParent


class Set(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Set, self).__init__("Trusted roles set")

    def run(self, message):
        if GetPermission.check_if_owner(message) is False:
            ret = "I apologise but only the discord guild owner may use this instruction\n"
            ret += "The owner of the discord guild can add allowed roles using the `" + self.commandline_config.first_keyword + " trusted-roles` instruction\n"
            return ret
        roles = []
        for role in message.role_mentions:
            if role not in roles:
                roles.append(role)
        if len(roles) is 0:
            return "you need to ping the roles in order to allow me to identify them, I could not find any pinged roles in the instruction"
        self.database_access.set_trusted_roles(message.guild.id, roles)
        ret = "set the following roles to be able to edit the auto translation settings :\n"
        role_names = []
        for role_mention in message.role_mentions:
            if role_mention.name not in role_names:
                role_names.append(role_mention.name)
        ret += "\n".join(role_names)
        return ret

    def get_description(self) -> str:
        return "trusted roles set description todo"

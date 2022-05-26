from src.instructions.instruction_inheritance import InstructionParent


class Help(InstructionParent):
    def __init__(self, commandline_config):
        self.commandline_config = commandline_config
        super(Help, self).__init__("Trusted Roles Help")

    def run(self, message):
        ret = "This is the `trusted-roles` option\n"
        ret += "\n"
        ret += "This instruction allows you to set who is allowed to change the auto translation settings for your " \
               "channels\n"
        ret += "By default there are no roles configured and only the server owner can setup the auto translations\n"
        ret += "Please note that only the discord guild owner may use these settings ( other users will be ignored )\n"
        ret += "\n"
        ret += "The understood instructions are as follow :\n"
        ret += "\n"
        ret += "`" + self.commandline_config.first_keyword + " trusted-roles set [roles]` sets roles to be allowed to " \
               "change the auto translation settings\n"
        ret += "the **[roles]** needs to be replaced with the roles that are to be given permission\n"
        ret += "usage example : `" + self.commandline_config.first_keyword + " trusted-roles set " \
               "\\@auto-translation-role` this sets the users with the role \@auto-translation-role to be allowed to " \
               "edit the auto-translation settings\n"
        ret += "\n"
        ret += "`" + self.commandline_config.first_keyword + " auto-translate get` displays the roles that are allowed " \
               "to change the auto translation settings ( it does not ping them )\n"
        ret += "\n"
        ret += "`" + self.commandline_config.first_keyword + " auto-translate remove [roles]` removes given roles from " \
               "the allowed to change the auto translation\n"
        ret += "Usage is the same as the `set` instruction\n"
        ret += "Please note that the server owner will still be able to change te settings regardless of the roles he " \
               "has or has not\n"
        return ret

    def get_description(self) -> str:
        return "this instruction implementation shows you how to use the `trusted-roles` option"

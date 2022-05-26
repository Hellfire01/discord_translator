from src.instructions.instruction_implementation.comon.get_permission import GetPermission
from src.instructions.instruction_inheritance import InstructionParent


class Get(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Get, self).__init__("Auto translation Get")

    def run(self, message):
        if GetPermission.check_if_owner(message) is False:
            ret = "I apologise but only the discord guild owner may use this instruction\n"
            ret += "The owner of the discord guild can add allowed roles using the `" + self.commandline_config.first_keyword + " trusted-roles` instruction\n"
            return ret
        channel = self.database_access.get_channel_instruction(message.channel.id)
        if channel is None:
            return "There is currently no auto translation enabled on the channel"
        else:
            return "The current auto translation setting for this channel is : " + channel.lang_string_instruction

    def get_description(self) -> str:
        return "This instruction will display the settings being applied in the current channel"

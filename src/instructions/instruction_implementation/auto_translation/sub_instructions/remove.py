from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Remove(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Remove, self).__init__("Auto translation Remove")

    def run(self, message):
        self.database_access.remove_channel_instruction(message.channel.id)
        return "Current channel was removed from all auto translation"

    def get_description(self) -> str:
        ret = "This instruction will remove this channel from the list of managed channels.\n"
        ret += "This removes the auto translation for this channel"
        return ret

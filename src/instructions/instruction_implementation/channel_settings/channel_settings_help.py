from src.global_settings import GlobalSettings
from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class ChannelSettingsHelp(InstructionParent):
    def __init__(self):
        super(ChannelSettingsHelp, self).__init__("Channel Settings Help")

    def run(self, message):
        ret = "This is the `channel-settings` option\n"
        ret += "This is where you configure a channel ( the current one ) in order to have a fully automated translation\n"
        return ret

    def get_description(self) -> str:
        return "this instruction_implementation shows you how to use the `channel-settings` option"

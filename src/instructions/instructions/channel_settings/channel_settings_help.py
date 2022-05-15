from src.global_settings import GlobalSettings
from src.instructions.instructions.instruction_parent import InstructionParent


class ChannelSettingsHelp(InstructionParent):
    def __init__(self):
        super(ChannelSettingsHelp, self).__init__("Channel Settings Help")

    def run(self, message):
        ret = "This is the `translate` option\n"
        ret += "Currently it is on TODO status\n"
        return ret

    def get_description(self) -> str:
        return "this instructions shows you how to use the `channel-settings` option"

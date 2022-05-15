from src.global_settings import GlobalSettings
from src.instructions.instructions.instruction_parent import InstructionParent
from src.instructions.instructions.translate.google_translate_api import GoogleTranslateApi


class ChannelSettingsSubInstruction(InstructionParent):
    def __init__(self, channel_settings_help_instruction):
        self.channel_settings_help_instruction = channel_settings_help_instruction
        self.googleTranslateApi = GoogleTranslateApi()
        super(ChannelSettingsSubInstruction, self).__init__("Channel settings Instruction")

    def run(self, message) -> str:
        ret = "not yet implemented"
        return ret

    def get_description(self):
        return "use `" + GlobalSettings.get_instance().instruction_keyword[0] + " channel-settings help` in order to" \
                                                                                "know how to use this instruction"

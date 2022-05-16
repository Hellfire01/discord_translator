from src.global_settings import GlobalSettings
from src.instructions.instruction_implementation.instruction_parent import InstructionParent
from src.instructions.instruction_implementation.not_an_instruction import NotAnInstruction
from src.instructions.instruction_management.sub_instruction_extractor import SubInstructionExtractor
from src.instructions.instruction_management.instruction_referencer import InstructionReferencer
from src.instructions.instruction_management.instruction_container import InstructionContainer
from src.instructions.instruction_implementation.channel_settings.channel_settings_help import ChannelSettingsHelp
from src.instructions.instruction_implementation.channel_settings.channel_settings_sub_instruction import ChannelSettingsSubInstruction


class ChannelSettings(InstructionParent):
    def __init__(self):
        super(ChannelSettings, self).__init__("Channel Settings")
        channel_settings_help_instruc = "`" + GlobalSettings.get_instance().instruction_keyword[0] + " channel settings help`"
        channel_settings_help = ChannelSettingsHelp()
        nai = NotAnInstruction("The `channel-settings` instruction needs arguments in order to work\nUse `" +
                               GlobalSettings.get_instance().instruction_keyword[0] + " channel-settings help`"
                               " to see how to use this option")
        instruction_referencer = InstructionReferencer(help_instruction=channel_settings_help,
                                                       not_an_instruction=nai,
                                                       default_instruction=ChannelSettingsSubInstruction(channel_settings_help_instruc))
        instruction_referencer.add_instruction(InstructionContainer(["-h", "help", "--help"], channel_settings_help))

        self.instruction_extractor = SubInstructionExtractor([], instruction_referencer)

    def run(self, message) -> str:
        s_message = " ".join(message.strip().split(" ")[2:])
        instruction = self.instruction_extractor.get_instruction(s_message)
        ret = instruction.run(s_message)
        return ret

    def get_description(self):
        ret = "this instruction is used in order to set up automated translation for a channel\n"
        ret += "in order to use get ore information on this instruction, use `" + GlobalSettings.get_instance().instruction_keyword[0] + " channel-settings help`"
        return ret

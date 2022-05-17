from src.global_settings import GlobalSettings
from src.instructions.instruction_implementation.instruction_parent import InstructionParent
from src.instructions.instruction_implementation.not_an_instruction import NotAnInstruction
from src.instructions.instruction_management.sub_instruction_extractor import SubInstructionExtractor
from src.instructions.instruction_management.instruction_referencer import InstructionReferencer
from src.instructions.instruction_management.instruction_container import InstructionContainer
from src.instructions.instruction_implementation.auto_translation.sub_instructions.help import Help
from src.instructions.instruction_implementation.auto_translation.sub_instructions.sub_instruction import SubInstruction
from src.instructions.instruction_implementation.instruction_list import InstructionList
from src.instructions.instruction_implementation.auto_translation.sub_instructions.get import Get
from src.instructions.instruction_implementation.auto_translation.sub_instructions.set import Set
from src.instructions.instruction_implementation.auto_translation.sub_instructions.remove import Remove


class AutoTranslation(InstructionParent):
    def __init__(self):
        super(AutoTranslation, self).__init__("Auto Translation")
        channel_settings_help_instruc = "`" + GlobalSettings.get_instance().instruction_keyword[0] + " auto translation help`"
        channel_settings_help = Help()
        nai = NotAnInstruction("The `auto-translation` instruction needs arguments in order to work\nUse `" +
                               GlobalSettings.get_instance().instruction_keyword[0] + " auto-translation help`"
                               " to see how to use this option")
        instruction_referencer = InstructionReferencer(help_instruction=channel_settings_help,
                                                       not_an_instruction=nai,
                                                       default_instruction=SubInstruction(channel_settings_help_instruc))
        instruction_referencer.add_instruction(InstructionContainer(["-h", "help", "--help"], channel_settings_help))
        instruction_referencer.add_instruction(InstructionContainer(["-s", "set", "--set"], Set()))
        instruction_referencer.add_instruction(InstructionContainer(["-g", "get", "--get"], Get()))
        instruction_referencer.add_instruction(InstructionContainer(["-r", "remove", "--remove"], Remove()))
        instruction_referencer.add_instruction(InstructionContainer(["-l", "list", "--list"], InstructionList(instruction_referencer.get_instruction_list, "Auto translation ")))
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

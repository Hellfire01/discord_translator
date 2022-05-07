from src.global_settings import GlobalSettings
from src.instructions.instructions.instruction_parent import InstructionParent
from src.instructions.instructions.not_an_instruction import NotAnInstruction
from src.instructions.instruction_management.sub_instruction_extractor import SubInstructionExtractor
from src.instructions.instruction_management.instruction_referencer import InstructionReferencer
from src.instructions.instruction_management.instruction_container import InstructionContainer
from src.instructions.instructions.translate.translate_help import TranslateHelp
from src.instructions.instructions.translate.translate_sub_instruction import TranslateSubInstruction


class Translate(InstructionParent):
    def __init__(self):
        super(Translate, self).__init__("Translate")
        trans_help_instruc = "`" + GlobalSettings.get_instance().instruction_keyword[0] + " translate help`"
        trans_lang_list_instruc = "`" + GlobalSettings.get_instance().instruction_keyword[0] + " lang-list`"
        translate_help = TranslateHelp()
        nai = NotAnInstruction("The `translate` instruction needs arguments in order to work\nUse `" +
                               GlobalSettings.get_instance().instruction_keyword[0] + " translate help`"
                               " to see how to use this option")
        instruction_referencer = InstructionReferencer(help_instruction=translate_help,
                                                       not_an_instruction=nai,
                                                       default_instruction=TranslateSubInstruction(trans_help_instruc, trans_lang_list_instruc))
        instruction_referencer.add_instruction(InstructionContainer(["-h", "help", "--help"], translate_help))
        self.instruction_extractor = SubInstructionExtractor([], instruction_referencer)

    def run(self, message) -> str:
        s_message = " ".join(message.strip().split(" ")[2:])
        instruction = self.instruction_extractor.get_instruction(s_message)
        ret = instruction.run(s_message)
        return ret

    def get_description(self):
        ret = "this instruction is used for a manual translation\n"
        ret += "in order to use get ore information on this instruction, use `" + GlobalSettings.get_instance().instruction_keyword[0] + " translate help`"
        return ret

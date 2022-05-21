from src.instructions.instruction_inheritance import InstructionParent
from src.instructions.instruction_implementation.generic_instructions.not_an_instruction import NotAnInstruction
from src.instructions.instruction_management.sub_instruction_extractor import SubInstructionExtractor
from src.instructions.instruction_management.instruction_referencer import InstructionReferencer
from src.instructions.instruction_management.instruction_container import InstructionContainer
from src.instructions.instruction_implementation.translate.translate_help import TranslateHelp
from src.instructions.instruction_implementation.translate.translate_sub_instruction import TranslateSubInstruction


class Translate(InstructionParent):
    def __init__(self, commandline_config, translate_config, google_translate_api):
        self.commandline_config = commandline_config
        self.translate_config = translate_config
        super(Translate, self).__init__("Translate")
        trans_help_instruc = "`" + self.commandline_config.first_keyword + " translate help`"
        trans_lang_list_instruc = "`" + self.commandline_config.first_keyword + " lang-list`"
        translate_help = TranslateHelp(self.commandline_config, self.translate_config)
        nai_string = "The `translate` instruction needs arguments in order to work\nUse `" + self.commandline_config.first_keyword + " translate help` to see how to use this option"
        nai = NotAnInstruction(nai_string)
        translate_si = TranslateSubInstruction(commandline_config, translate_config, google_translate_api, trans_help_instruc, trans_lang_list_instruc)
        instruction_referencer = InstructionReferencer(commandline_config, translate_help, not_an_instruction=nai, default_instruction=translate_si)
        instruction_referencer.add_instruction(InstructionContainer(["-h", "help", "--help"], translate_help))
        self.instruction_extractor = SubInstructionExtractor([], instruction_referencer)

    def run(self, message) -> str:
        s_message = " ".join(message.content.strip().split(" ")[2:])
        instruction = self.instruction_extractor.get_instruction(s_message)
        ret = instruction.run(s_message)
        return ret

    def get_description(self):
        ret = "this instruction is used for a manual translation\n"
        ret += "in order to use get ore information on this instruction, use `" + self.commandline_config.first_keyword + " translate help`"
        return ret

from src.instructions.instruction_inheritance.automated_instruction_parent import AutomatedInstructionParent
from src.instructions.instruction_implementation.auto_translation.common.lang_instruction import LangInstruction


class AutomatedTranslationExec(AutomatedInstructionParent):
    def __init__(self, logger, database_access, commandline_config, google_translate_api):
        self.logger = logger
        self.database_access = database_access
        self.commandline_config = commandline_config
        self.google_translate_api = google_translate_api
        super(AutomatedTranslationExec, self).__init__("Automated translation")

    def run(self, message) -> str:
        channel_instruction = self.database_access.get_channel_instruction(message.channel.id)
        if channel_instruction is None:
            return ""
        else:
            ret = ""
            output_langs = LangInstruction.get_langs_from_instruction(self.logger, message.channel.id, channel_instruction.lang_string_instruction)
            for output_lang in output_langs:
                ret += "\n" + output_lang.emotes[0] + " " + self.google_translate_api.translate(message.content, None, output_lang)
            return ret

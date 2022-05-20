from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class SubInstruction(InstructionParent):
    def __init__(self, commandline_config, channel_settings_help_instruction):
        self.commandline_config = commandline_config
        self.channel_settings_help_instruction = channel_settings_help_instruction
        super(SubInstruction, self).__init__("Auto translation Instruction")

    def run(self, message) -> str:
        ret = "not yet implemented"
        return ret

    def get_description(self):
        return "use `" + self.commandline_config.first_keyword + " auto-translation help` in order to know how to use" \
                                                                 "this instruction"

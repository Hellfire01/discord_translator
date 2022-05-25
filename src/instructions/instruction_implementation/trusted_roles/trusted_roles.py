from src.instructions.instruction_inheritance import InstructionParent
from src.instructions.instruction_implementation.generic_instructions.not_an_instruction import NotAnInstruction
from src.instructions.instruction_management.sub_instruction_extractor import SubInstructionExtractor
from src.instructions.instruction_management.instruction_referencer import InstructionReferencer
from src.instructions.instruction_management.instruction_container import InstructionContainer
from src.instructions.instruction_implementation.trusted_roles.sub_instructions.help import Help
from src.instructions.instruction_implementation.trusted_roles.sub_instructions.sub_instruction import SubInstruction
from src.instructions.instruction_implementation.trusted_roles.sub_instructions.get import Get
from src.instructions.instruction_implementation.trusted_roles.sub_instructions.set import Set
from src.instructions.instruction_implementation.trusted_roles.sub_instructions.remove import Remove
from src.instructions.instruction_implementation.instruction_list import InstructionList



class TrustedRoles(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        super(TrustedRoles, self).__init__("Trusted Roles")
        trusted_roles_help_instruc = "`" + self.commandline_config.first_keyword + " trusted-roles help`"
        trusted_roles_help = Help()
        nai = NotAnInstruction(commandline_config, "The `trusted-roles` instruction needs arguments in order to work\nUse `" + self.commandline_config.first_keyword + " trusted-roles help` to see how to use this option")
        sub_instruction = SubInstruction(commandline_config, trusted_roles_help_instruc)
        instruction_referencer = InstructionReferencer(commandline_config, trusted_roles_help, not_an_instruction=nai, default_instruction=sub_instruction)
        instruction_referencer.add_instruction(InstructionContainer(["-h", "help", "--help"], trusted_roles_help))
        instruction_referencer.add_instruction(InstructionContainer(["-s", "set", "--set"], Set(commandline_config, database_access)))
        instruction_referencer.add_instruction(InstructionContainer(["-g", "get", "--get"], Get(commandline_config, database_access)))
        instruction_referencer.add_instruction(InstructionContainer(["-r", "remove", "--remove"], Remove(commandline_config, database_access)))
        instruction_referencer.add_instruction(InstructionContainer(["-l", "list", "--list"], InstructionList(instruction_referencer.get_instruction_list, "Auto translation ")))
        self.instruction_extractor = SubInstructionExtractor([], instruction_referencer)

    def run(self, message) -> str:
        s_message = " ".join(message.content.strip().split(" ")[2:])
        instruction = self.instruction_extractor.get_instruction(s_message)
        ret = instruction.run(message)
        return ret

    def get_description(self):
        ret = "this instruction is used in order to tell the translator what are the roles that are allowed to set up / edit / remove the automated translation channels\n"
        ret += "in order to use get ore information on this instruction, use `" + self.commandline_config.first_keyword + " trusted-roles help`"
        return ret

from src.instructions.instruction_implementation.comon.get_permission import GetPermission
from src.instructions.instruction_inheritance import InstructionParent


class Get(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Get, self).__init__("Trusted roles get")

    def run(self, message):
        return "todo"

    def get_description(self) -> str:
        return "trusted roles get description todo"

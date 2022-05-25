from src.instructions.instruction_inheritance import InstructionParent


class Remove(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Remove, self).__init__("Trusted roles remove")

    def run(self, message):
        return "trusted roles remove todo"

    def get_description(self) -> str:
        return "trusted roles remove description todo"

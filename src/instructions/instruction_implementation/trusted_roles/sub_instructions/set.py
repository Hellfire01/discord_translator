from src.instructions.instruction_inheritance import InstructionParent


class Set(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Set, self).__init__("Trusted roles set")

    def run(self, message):
        return "trusted roles set todo"

    def get_description(self) -> str:
        return "trusted roles set description todo"

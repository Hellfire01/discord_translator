from src.instructions.instruction_implementation.instruction_parent import InstructionParent


class Get(InstructionParent):
    def __init__(self, commandline_config, database_access):
        self.commandline_config = commandline_config
        self.database_access = database_access
        super(Get, self).__init__("Auto translation Get")

    def run(self, message):
        split_message = " ".join(message.content.strip().split(" ")[3:])
        return "Auto translation get todo"

    def get_description(self) -> str:
        return "This instruction will display the settings being applied in the current channel"

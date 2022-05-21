from src.instructions.instruction_inheritance.automated_instruction_parent import AutomatedInstructionParent


class AutomatedTranslationExec(AutomatedInstructionParent):
    def __init__(self, database_access):
        self.database_access = database_access
        super(AutomatedTranslationExec, self).__init__("Automated translation")

    def run(self, message):
        pass

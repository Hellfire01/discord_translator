

class LangInstruction:
    @staticmethod
    def get_langs_from_instruction(instruction):
        pass

    @staticmethod
    def get_instruction_from_langs(langs) -> str:
        return " / ".join([e.name for e in langs])

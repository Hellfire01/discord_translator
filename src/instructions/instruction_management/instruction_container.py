

class InstructionContainer:
    def __init__(self, keywords, reference):
        self.keywords = keywords
        self.reference = reference

    def __lt__(self, other):
        return self.keywords[0] < other.keywords[0]

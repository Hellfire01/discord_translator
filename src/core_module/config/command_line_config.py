

class CommandLineConfig:
    def __init__(self, keywords):
        self.__keywords = keywords
        self.__first_keyword = keywords[0]

    @property
    def keywords(self):
        return self.__keywords

    @property
    def first_keyword(self):
        return self.__first_keyword

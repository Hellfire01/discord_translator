from src.security.filters.filter_parent import FilterParent
from src.security.filter_exception import FilterException


class NoTagsFilter(FilterParent):
    def filter(self, message):
        if message.mention_everyone:
            raise FilterException("I am sorry but I cannot translate messages with the @ everyone mention")

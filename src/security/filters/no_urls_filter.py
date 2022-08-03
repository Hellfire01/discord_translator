import re
from src.security.filters.filter_parent import FilterParent
from src.security.filter_exception import FilterException


class NoUrlsFilter(FilterParent):
    def __init__(self):
        super(NoUrlsFilter, self).__init__()

    def __has_url(self, string):
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, string)
        return len(url) == 0

    def filter(self, message):
        if self.__has_url(message.content):
            raise FilterException("I am sorry but I cannot translate messages with urls inside")

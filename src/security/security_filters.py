from src.security.filters.filter_parent import FilterParent


class SecurityFilter:
    def __init__(self):
        self.__filters = []

    def add_filter(self, filter_: FilterParent):
        self.__filters.append(filter_)

    def filter(self, message):
        for filter_ in self.__filters:
            filter_.filter(message)

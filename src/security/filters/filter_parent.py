
class FilterParent:
    def __init__(self):
        pass

    def filter(self, message) -> str:
        raise RuntimeError("Method not properly overloaded")

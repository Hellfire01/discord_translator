from dataclasses import dataclass


@dataclass
class Lang:
    emotes: list
    name: str
    acronym: str

    def __hash__(self):
        return hash("/".join(self.emotes) + " " + self.name + " " + self.acronym)

    def __lt__(self, other):
        return self.name < other.name

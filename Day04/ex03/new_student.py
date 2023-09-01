import random
import string
from dataclasses import dataclass, field


def generateID() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generateID)

    def __post_init__(self):
        if (len(self.name) == 0):
            self.name = "ChillMan"
        if (len(self.surname) == 0):
            self.surname = "CoolGirl"
        self.login = self.name[0] + self.surname.lower()
from dataclasses import dataclass


class Node:
    def get(self, number):
        if not isinstance(number, list):
            number = list(map(int, reversed(number.split('.'))))
        e = self.children[number.pop() - 1]
        if number:
            return e.get(number)
        return e


@dataclass
class CodingScheme(Node):
    children: list = None
    elements: list = None

    def __post_init__(self):
        if self.children is None:
            self.children = []
        if self.elements is None:
            self.elements = []
        self.a = []

    def __iter__(self):
        return iter(self.elements)

    def append(self, level, name, data=None):
        if len(self.a) - 1 > level:
            n = len(self.a) - 1 - level
            del self.a[-n:]

        if len(self.a) <= level:
            self.a.append(1)
        else:
            self.a[level] += 1

        number = '.'.join(map(str, self.a))

        element = Element(name, number, level, data)
        self.elements.append(element)
        if level == 0:
            self.children.append(element)
        else:
            self.get(self.a[:-1]).append(element)


@dataclass
class Element(Node):
    name: str
    number: str
    level: int
    data: dict = None
    children: list = None

    def __post_init__(self):
        if self.children is None:
            self.children = []
        if self.data is None:
            self.data = {}

    def append(self, element):
        self.children.append(element)

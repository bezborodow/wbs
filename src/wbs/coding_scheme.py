from dataclasses import dataclass
from .node import Node
from .element import Element


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
        '''
        Append a new element to the WBS.
        0 is the top level.
        '''

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

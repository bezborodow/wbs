from dataclasses import dataclass
from .node import Node
from .element import Element


@dataclass
class CodingScheme(Node):
    '''
    Represents a work breakdown structure coding scheme.
    '''

    children: list = None
    elements: list = None


    def __post_init__(self):
        if self.children is None:
            self.children = []
        if self.elements is None:
            self.elements = []
        self.a = []


    def __iter__(self):
        '''
        Iterator for coding scheme elements.
        '''
        return iter(self.elements)


    def append(self, name, level=0, data=None):
        '''
        Append a new element to the work breakdown structure coding scheme.

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


    @classmethod
    def fromfile(cls, file):
        '''
        Import a work breakdown structure from a file.

        Levels are indicated by indentations of 4 spaces. Numbering is applied
        automatically.
        '''

        scheme = cls()
        for line in file:
            line = line.rstrip().expandtabs(4)
            level = line.count('    ')
            name = line.lstrip()
            scheme.append(name, level)
        return scheme

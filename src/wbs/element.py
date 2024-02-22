from dataclasses import dataclass
from .node import Node


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

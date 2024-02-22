class Node:
    def get(self, number):
        if not isinstance(number, list):
            number = list(map(int, reversed(number.split('.'))))
        e = self.children[number.pop() - 1]
        if number:
            return e.get(number)
        return e

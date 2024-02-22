class Node:
    def get(self, number):
        '''
        Get a node based on the number string.
        '''

        # Convert number string '1.32.2' to [1, 32, 2]
        if not isinstance(number, list):
            number = list(map(int, reversed(number.split('.'))))

        index = number[0] - 1
        e = self.children[index]

        number = number[1:]
        if number:
            return e.get(number)

        return e

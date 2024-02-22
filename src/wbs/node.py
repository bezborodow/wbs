class Node:
    def get(self, number):
        '''
        Get a node based on the number.
        '''

        # Convert number string '1.32.2' to [1, 32, 2]
        if type(number) == str:
            number = list(map(int, number.split('.')))

        index = number[0] - 1
        e = self.children[index]

        number = number[1:]
        if number:
            # Descend recursively.
            return e.get(number)

        return e

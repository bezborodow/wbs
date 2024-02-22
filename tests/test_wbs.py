import re
import unittest
from src.wbs import CodingScheme


class TestWorkBreakdownStructure(unittest.TestCase):
    def lines(self, text):
        '''
        Returns a list of lines from a multiline string with
        whitespace removed.
        '''
        return list(map(lambda l: l.strip(), text.splitlines()))[1:-1]


    def test_scheme(self):
        scheme = CodingScheme()
        scheme.append(0, 'Aircraft System')
        scheme.append(1, 'Air Vehicle')
        scheme.append(2, 'Air Frame')
        scheme.append(2, 'Propulsion')
        scheme.append(2, 'Application Software')
        scheme.append(1, 'SE Program Mgmt')
        scheme.append(1, 'System T&E')
        scheme.append(2, 'DT&E')
        scheme.append(2, 'OT&E')
        scheme.append(2, 'Mockups')
        scheme.append(0, 'Fire Control')
        scheme.append(1, 'Radar')
        scheme.append(2, 'Receiver')
        scheme.append(2, 'Transmitter')
        scheme.append(2, 'Antenna')
        scheme.append(2, 'Radar S/W')

        expected = self.lines('''
            1 Aircraft System
            1.1 Air Vehicle
            1.1.1 Air Frame
            1.1.2 Propulsion
            1.1.3 Application Software
            1.2 SE Program Mgmt
            1.3 System T&E
            1.3.1 DT&E
            1.3.2 OT&E
            1.3.3 Mockups
            2 Fire Control
            2.1 Radar
            2.1.1 Receiver
            2.1.2 Transmitter
            2.1.3 Antenna
            2.1.4 Radar S/W
        ''')
        self.assertEqual(16, len(expected))

        actual = []
        for element in scheme:
            actual.append(f'{element.number} {element.name}')

        element = scheme.get([2, 1, 4])
        self.assertEqual('2.1.4', element.number)
        self.assertEqual('Radar S/W', element.name)
        self.assertEqual(element, scheme.get('2.1.4'))

        self.assertEqual(16, len(actual))
        for i, line in enumerate(actual):
            self.assertEqual(expected[i], actual[i])
            m = re.match(r'^([0-9.]+) (.*)$', line)
            number = m.group(1)
            name = m.group(2)
            element = scheme.get(number)
            self.assertEqual(number, element.number)
            self.assertEqual(name, element.name)


if __name__ == '__main__':
    unittest.main()

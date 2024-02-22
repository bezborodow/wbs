import re
import unittest
from src.wbs import CodingScheme


class TestWorkBreakdownStructure(unittest.TestCase):
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

        actual = []
        for element in scheme:
            actual.append(f'{element.number} {element.name}')
        self.assertEqual(16, len(actual))

        element = scheme.get([2, 1, 4])
        self.assertEqual('2.1.4', element.number)
        self.assertEqual('Radar S/W', element.name)
        self.assertEqual(element, scheme.get('2.1.4'))

        i = 0
        with open('tests/data/SYSTEMS', 'r') as file:
            for line in file:
                self.assertEqual(line.strip(), actual[i])
                m = re.match(r'^([0-9.]+) (.*)$', line)
                number = m.group(1)
                name = m.group(2)
                element = scheme.get(number)
                self.assertEqual(number, element.number)
                self.assertEqual(name, element.name)
                i += 1


if __name__ == '__main__':
    unittest.main()

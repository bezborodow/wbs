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

        for element in scheme:
            print(element)


if __name__ == '__main__':
    unittest.main()

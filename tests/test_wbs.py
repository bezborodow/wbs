import unittest
from src.wbs import wbs

class TestWorkBreakdownStructure(unittest.TestCase):
    def test_hi(self):
        self.assertEqual(3, wbs.add_one(2))

if __name__ == '__main__':
    unittest.main()

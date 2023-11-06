import program
import unittest

class TestSum(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.absoluteValue(2), 2)

if __name__ == '__main__':
    unittest.main()
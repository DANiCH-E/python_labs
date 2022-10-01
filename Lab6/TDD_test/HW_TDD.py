import unittest
import sys, os

sys.path.append(os.getcwd())
from Lab6.HW import *

class Calc_Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(final('+', -2, 1), -1)
    def test_2(self):
        self.assertEqual(final('-', 5, 1), 4)
if __name__ == "__main__":
    unittest.main()
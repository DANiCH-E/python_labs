import unittest
import sys, os
from builder import *

sys.path.append(os.getcwd())

class Furniture_Builder_Test(unittest.TestCase):
    director = Director()
    builder = Furniture_Builder()
    director.builder = builder
    def test_Lasurit(self):
       print("Лазурит: ")
       self.director.Lasurit()
       self.builder.product.list_parts()

    def test_Shatura(self):
        print("\nШатура: ")
        self.director.Shatura()
        self.builder.product.list_parts()

if __name__ == "__main__":
    unittest.main()
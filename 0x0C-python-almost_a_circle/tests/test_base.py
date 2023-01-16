#!/usr/bin/python3
"""This is a unittest for the class Base:

    Tests run to test the instantiation of attributes in Base class

    """


import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_no_args(self):
        emp1 = Base()
        emp2 = Base()
        emp3 = Base(12)
        self.assertEqual(emp1.id, 1)
        self.assertEqual(emp2.id, 2)
        self.assertEqual(emp3.id, 12)

if __name__ == "__main__":
    unnitest.main()

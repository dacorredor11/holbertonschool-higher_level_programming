#!/usr/bin/python3
"""Unittest for Base class"""

import json
import os
from os import path
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This class is for testing the Base class"""

    @classmethod
    def setUpClass(cls):
        """Set up instances for all tests"""
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base(11)
        cls.b3 = Base(9)
        cls.b4 = Base()
        cls.b5 = Base()
        cls.b6 = Base("random")
        cls.b7 = Base(11.1)
        cls.b8 = Base(None)
        cls.r1 = Rectangle(10, 7, 2, 8)

    def test_id_validation(self):
        """Test to check id's"""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 11)
        self.assertEqual(self.b3.id, 9)
        self.assertEqual(self.b4.id, 2)
        self.assertEqual(self.b5.id, 3)
        self.assertEqual(self.b6.id, "random")
        self.assertEqual(self.b7.id, 11.1)
        self.assertEqual(self.b8.id, 4)

    def test_to_json_string(self):
        """Test to check to_json_string function"""

        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

        dictionary = self.r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])

        self.assertTrue(type(json_string) is str)
        test_dict = json.loads(json_string)
        self.assertEqual(test_dict, [dictionary])

    def test_from_json_string(self):
        """Test to check from_json_string function"""

        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])

    @classmethod
    def tearDownClass(cls):
        """class method called after tests have run"""

        pass


if __name__ == "__main__":
    unittest.main()

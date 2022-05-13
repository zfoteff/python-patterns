__author__ = "Zac Foteff"
__version__ = "v1.0.0"

import unittest
from singleton import singleton

class singleton_tests(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_create_single_instance(self):
        self.assertTrue(True)

    def multiple_instances_return_equal(self):
        pass
"""Singleton class unit tests"""
__author__ = "Zac Foteff"
__version__ = "v1.0.0"

import unittest
import time
from bin.logger import Logger
from singleton.singleton import Singleton

log = Logger("singleton_test")


class singleton_tests(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_constructor_raises_runtime_error(self):
        """Assert that attempting to instantiate a new singleton object yields a runtime error"""
        with self.assertRaises(RuntimeError):
            Singleton()

    def test_retrieve_instance(self):
        start_time = time.perf_counter()
        i1 = Singleton.instance()
        self.assertIsNotNone(i1)
        self.assertIsInstance(i1, Singleton)
        elapsed_time = time.perf_counter() - start_time
        log("Completed retrieve instances test in {elapsed_time:.3f} seconds")
        Singleton.recycle()

    def test_retrieve_instance_objects(self):
        start_time = time.perf_counter()
        i1 = Singleton.instance()
        i1_objs = i1.get_objects()
        self.assertIsNotNone(i1_objs)
        self.assertEqual(i1_objs, {})
        self.assertIsInstance(i1_objs, dict)
        elapsed_time = time.perf_counter() - start_time
        log("Completed retrieve instances test in {elapsed_time:.3f} seconds")
        Singleton.recycle()

    def test_append_to_object(self):
        start_time = time.perf_counter()
        i1 = Singleton.instance()
        i1.append(1, "a")
        self.assertEqual(1, len(i1.get_objects()))
        self.assertIn(1, i1.get_objects().keys())
        elapsed_time = time.perf_counter() - start_time
        log("Completed retrieve instances test in {elapsed_time:.3f} seconds")
        Singleton.recycle()

    def test_multiple_instances_return_same_obj(self):
        start_time = time.perf_counter()
        i1 = Singleton.instance()
        i2 = Singleton.instance()
        self.assertIs(i1, i2)
        elapsed_time = time.perf_counter() - start_time
        log(
            "Completed two instances return same object test in {elapsed_time:.3f} seconds"
        )

    def test_state_persists_across_instances(self):
        start_time = time.perf_counter()
        i1 = Singleton.instance()
        i2 = Singleton.instance()
        self.assertIs(i1, i2)
        self.assertIs(i1.get_objects(), i2.get_objects())
        self.assertEqual(0, len(i1.get_objects()))
        self.assertEqual(0, len(i2.get_objects()))
        i1.append(1, "a")
        self.assertEqual(1, len(i1.get_objects()))
        self.assertIn(1, i1.get_objects().keys())
        self.assertEqual(1, len(i2.get_objects()))
        self.assertIn(1, i2.get_objects().keys())
        elapsed_time = time.perf_counter() - start_time
        log("Completed retrieve instances test in {elapsed_time:.3f} seconds")
        Singleton.recycle()

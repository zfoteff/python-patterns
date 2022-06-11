__author__ = "Zac Foteff"
__version__ = "v1.0.0"

import unittest
from time import perf_counter as time
from builder.builder import PasswordBuilder
from bin.logger import Logger

log = Logger("builderTests")


class BuilderTests(unittest.TestCase):
    """Test suite for the Builder class"""

    def setUp(self) -> None:
        return super().setUp()

    def test_create_builder_object(self):
        start_time = time()
        elapsed_time = time() - start_time
        log(f"[+] Completed builder object instance test in {elapsed_time:.3f} seconds")

    def test_default_build_result(self):
        start_time = time()
        elapsed_time = time() - start_time
        log(f"[+] Completed builder object instance test in {elapsed_time:.3f} seconds")

    def tests_proper_characters_included(self):
        start_time = time()
        elapsed_time = time() - start_time
        log(f"[+] Completed builder object instance test in {elapsed_time:.3f} seconds")

if __name__ == "__main__":
    unittest.main()
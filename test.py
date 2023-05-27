import unittest
import a
import math

class TestClass(unittest.TestCase):
    def test_add(self):
        manager = a.OperationsManager(1, 0)
        result = manager.perform_division()
        self.assertTrue(math.isnan(result))

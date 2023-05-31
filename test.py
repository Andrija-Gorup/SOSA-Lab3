import unittest
import a_fixed
import math

class TestClass(unittest.TestCase):
    def test_add(self):
        manager = a_fixed.OperationsManager(1, 0)
        result = manager.perform_division()
        self.assertTrue(math.isnan(result))

    def test_list_1(self):
        manager = a_fixed.OperationsManager(1, 10)
        result = manager.operation_1()
        self.assertTrue(math.isnan(result))

    def test_list_2(self):
        manager = a_fixed.OperationsManager(1, -11)
        result = manager.operation_1()
        self.assertTrue(math.isnan(result))

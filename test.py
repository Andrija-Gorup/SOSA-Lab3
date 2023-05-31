import unittest
import a
import math

class TestClass(unittest.TestCase):
    def test_add(self):
        manager = a.OperationsManager(1, 0)
        result = manager.perform_division()
        self.assertTrue(math.isnan(result))

    def test_list_1(self):
        manager = a.OperationsManager(1, 10)
        result = manager.operation_1()
        self.assertTrue(math.isnan(result))

    def test_list_2(self):
        manager = a.OperationsManager(1, -11)
        result = manager.operation_1()
        self.assertTrue(math.isnan(result))

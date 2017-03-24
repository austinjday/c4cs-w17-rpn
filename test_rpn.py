import unittest
import rpn


class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_add_custom(self):
        result = rpn.calculate('0 25 +')
        self.assertEqual(25, result)

    def test_subtract(self):
        result = rpn.calculate('10 2 -')
        self.assertEqual(8, result)

    def test_exp_tdd(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)

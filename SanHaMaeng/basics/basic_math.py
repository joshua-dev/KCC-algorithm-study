# 1.9 Code Challenge!

# Implent those seven basic functions

# - sum (+)
# - difference (-)
# - product (*)
# - quotient (/)
# - floored quotient (//)
# - remainder (%)
# - power (**)

import unittest


def sum(a, b):
    try:
        return a + b

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


def difference(a, b):
    try:
        return a - b if a > b else b - a

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


def product(a, b):
    try:
        return a * b

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


def quotient(a, b):
    try:
        return a / b

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


def flooredQuotient(a, b):
    try:
        return a // b

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


def remainder(a, b):
    try:
        return a % b

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


def power(a, b):
    try:
        if a == 0:
            if b == 0:
                raise ArithmeticError
            else:
                return 0

        else:
            result = 1
            for _ in range(b):
                result = product(result, a)

            return result

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


class BasicFunctionTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(3, 7), 10)
        self.assertEqual(sum(6, float('inf')), float('inf'))
        self.assertIsInstance(sum(6, '7'), str)

    def test_difference(self):
        self.assertEqual(difference(4, 3), 1)
        self.assertEqual(difference(1, float('-inf')), float('inf'))
        self.assertNotEqual(difference(1, 10), -9)
        self.assertIsInstance(difference(2, '8'), str)


if __name__ == '__main__':
    unittest.main()

def mult(m, n):
  try:
    return m * n

  except TypeError as TE:
    return TE.__str__()

  except ArithmeticError as AE:
    return AE.__str__()


curry = lambda func, var: lambda x: func(var, x)

mult_curry_prev = lambda m: curry(mult, m)

mult_curry = lambda n: mult_curry_prev(n)

import unittest

class CurryingTest(unittest.TestCase):
  def test_normal(self):
    self.

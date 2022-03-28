import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10"""
        output = """3628801"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """30"""
        output = """3628801"""
        self.assertIO(input, output)


def resolve():
  from math import gcd
  from functools import reduce
  def lcm_base(x, y):
    return (x * y) // gcd(x, y)

  def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

  N = int(input())
  print(lcm(*list(range(2, N+1)))+1)
resolve()

if __name__ == "__main__":
    unittest.main()

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
        input = """0 2 3 4 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 2 0 4 5"""
        output = """3"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product
import numpy as np

def resolve():
  x = [int(x) for x in input().split(" ")]
  for i, X in enumerate(x):
    if X == 0:
      print(i+1)
      return True


if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()

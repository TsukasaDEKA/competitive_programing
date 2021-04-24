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
        input = """3 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 2"""
        output = """Yes"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product
import numpy as np

def resolve():
  X, Y = map(int, input().split(" "))
  if Y%2 != 0:
    print("No")
    return True
  if Y < (2*X):
    print("No")
    return True
  if Y > (4*X):
    print("No")
    return True
  print("Yes")

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()

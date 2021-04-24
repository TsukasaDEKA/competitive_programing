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
        input = """6
4 0
5 8
0 1000000
0 0
1 0
1000000 1000000"""
        output = """0
3
1000000
0
1
0"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product
import numpy as np

def resolve():
  loop_n = int(input())
  for _ in range(loop_n):
    A, K = map(int, input().split(" "))
    if K >= A:
      print(K-A)
    elif (K+A)%2==0:
      print(0)
    else:
      print(1)

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
  unittest.main()
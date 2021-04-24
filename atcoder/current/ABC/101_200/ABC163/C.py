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
        input = """5
1 1 2 2"""
        output = """2
2
0
0
0"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """10
1 1 1 1 1 1 1 1 1"""
        output = """9
0
0
0
0
0
0
0
0
0"""
        self.assertIO(input, output)
    def test_Sample_Input_3(self):
        input = """7
1 2 3 4 5 6"""
        output = """1
1
1
1
1
1
0"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product
from collections import Counter

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  results = [0] * N
  for a in A:
    results[a-1] += 1
  for r in results:
    print(r)

# if __name__ == "__main__":
#   resolve()
resolve()

if __name__ == "__main__":
    unittest.main()
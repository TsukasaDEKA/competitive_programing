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
        input = """3 2
2
1 3
1
3"""
        output = """1"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """3 3
1
3
1
3
1
3"""
        output = """2"""
        self.assertIO(input, output)

from math import gcd
from functools import reduce
from itertools import product

def resolve():
  N, K = map(int, input().split(" "))

  a = []
  for k in range(K):
    d = int(input())
    a.extend([int(x) for x in input().split(" ")])

  a = list(set(a))
  print(N-len(a))

if __name__ == "__main__":
    resolve()

if __name__ == "__main__":
    unittest.main()
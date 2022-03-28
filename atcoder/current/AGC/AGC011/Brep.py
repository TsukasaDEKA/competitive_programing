import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """3
3 1 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
40 1 30 2 7 20"""
        output = """4"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])
  accA = [0] + list(accumulate(A))
  for i in reversed(range(N)):
    if accA[i]*2 < A[i]:
      print(N-i)
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
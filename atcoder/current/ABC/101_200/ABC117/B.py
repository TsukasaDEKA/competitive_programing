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
        input = """4
3 8 5 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
3 8 4 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
1 8 10 5 8 12 34 100 11 3"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])

  print("Yes" if sum(A[:-1]) > A[-1] else "No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
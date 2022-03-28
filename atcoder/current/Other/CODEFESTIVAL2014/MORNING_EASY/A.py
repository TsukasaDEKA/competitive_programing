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
4 3 2 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 2 3 5"""
        output = """1.33333333"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  print((A[-1]-A[0])/(N-1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
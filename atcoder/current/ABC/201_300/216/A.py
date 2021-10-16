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
        input = """15.8"""
        output = """15+"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1.0"""
        output = """1-"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """12.5"""
        output = """12"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  X, Y = map(int, input().split("."))
  if Y <= 2:
    print(X, "-", sep="")
  elif Y <= 6:
    print(X)
  else:
    print(X, "+", sep="")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
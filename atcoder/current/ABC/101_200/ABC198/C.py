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
        input = """5 15 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 11 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 4 4"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  from math import sqrt, ceil
  from decimal import Decimal
  R, X, Y = map(int, input().split(" "))
  D = sqrt(X*X + Y*Y)
  ans = ceil(D/R) if D >= R else 2

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

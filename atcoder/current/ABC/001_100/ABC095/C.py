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
        input = """1500 2000 1600 3 2"""
        output = """7900"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1500 2000 1900 3 2"""
        output = """8500"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1500 2000 500 90000 100000"""
        output = """100000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # AB ピザを min(X, Y) 分買って残りをバラで買う、
  # AB ピザを max(X, Y) 分買う
  # それぞれバラで買うの 3 パターンを比べる。
  A, B, C, X, Y = map(int, input().split(" "))
  ans = max(X, Y)*2*C
  ans = min(ans, min(X, Y)*2*C + (X-min(X, Y))*A + (Y-min(X, Y))*B)
  ans = min(ans, X*A + Y*B)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
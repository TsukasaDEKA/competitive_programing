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
        input = """1 10 10
3 5"""
        output = """2.857142857142857"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 10 10
3 2"""
        output = """0.0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 896 483
228 59
529 310
339 60
78 266
659 391"""
        output = """245.3080684596577"""
        self.assertIO(input, output)

def resolve():
  from math import ceil
  N, D, H = map(int, input().split(" "))
  ans = 0
  for _ in range(N):
    d, h = [int(x) for x in input().split(" ")]
    a = (H-h)/(D-d)
    b = H-D*a
    ans = max(ans, b)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()

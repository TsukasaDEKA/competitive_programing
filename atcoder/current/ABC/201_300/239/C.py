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
        input = """0 0 3 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """0 1 2 3"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000 1000000000 999999999 999999999"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  x1, y1, x2, y2 = [int(x) for x in input().split(" ")]
  dx = [2, 1, -1, -2]
  dy = [2, 1, -1, -2]
  d = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
  for i in range(8):
    dx_i, dy_i = d[i]
    for j in range(8):
      dx_j, dy_j = d[j]
      if x1+dx_i == x2+dx_j and y1+dy_i == y2+dy_j:
        print("Yes")
        return
  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
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
        input = """-1 -1
-1 2
3 2"""
        output = """3 -1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """-60 -40
-60 -80
-20 -80"""
        output = """-20 -40"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  X_Y = [[int(x) for x in input().split(" ")] for _ in range(3)]
  x_count = defaultdict(int)
  y_count = defaultdict(int)
  for i in range(3):
    x, y = X_Y[i]
    x_count[x]+=1
    y_count[y]+=1

  x, y = 0, 0

  for k, v in x_count.items():
    if v == 1:
      x = k

  for k, v in y_count.items():
    if v == 1:
      y = k

  print(x, y)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
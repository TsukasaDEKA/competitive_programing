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
SSRS"""
        output = """2 -1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20
SRSRSSRSSSRSRRRRRSRR"""
        output = """0 1"""
        self.assertIO(input, output)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def resolve():
  N = int(input())
  T = list(input())

  x, y = 0, 0
  i = 0
  for t in T:
    if t == "S":
      x+=dx[i]
      y+=dy[i]
    else:
      i+=1
      i%=4
  print(x, y)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
import sys
from io import StringIO
import unittest
from unittest.main import MAIN_EXAMPLES

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
2 3
1 1
4 1
RRL"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1
2 1
RR"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  inf = 10**18+1
  N = int(input())
  pos = defaultdict(list)
  for i in range(N):
    x, y = map(int, input().split(" "))
    pos[y].append((i, x))

  S = list(input())
  for y, per in pos.items():
    min_x_r = inf
    max_x_l = 0
    for i, x in per:
      if S[i] == "R":
        min_x_r = min(min_x_r, x)
      else:
        max_x_l = max(max_x_l, x)
    if max_x_l > min_x_r:
      print("Yes")
      return

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
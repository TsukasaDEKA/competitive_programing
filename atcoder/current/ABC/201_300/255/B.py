from email.policy import default
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
        input = """4 2
2 3
0 0
0 1
1 2
2 0"""
        output = """2.23606797749978969"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 1
2
-100000 -100000
100000 100000"""
        output = """282842.712474619009"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """8 3
2 6 8
-17683 17993
93038 47074
58079 -57520
-41515 -89802
-72739 68805
24324 -73073
71049 72103
47863 19268"""
        output = """130379.280458974768"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  from math import sqrt
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = set([int(x)-1 for x in input().split(" ")])
  POS = [[int(x) for x in input().split(" ")] for _ in range(N)]

  farest = defaultdict(int)
  for i in range(N):
    x, y = POS[i]

    diff = inf
    for a in A:
      x_, y_ = POS[a]
      new_diff = (x-x_)**2 + (y-y_)**2
      if diff > new_diff:
        diff = new_diff
    farest[a] = max(farest[a], diff)

  ans = 0
  for a in A:
    ans = sqrt(farest[a])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
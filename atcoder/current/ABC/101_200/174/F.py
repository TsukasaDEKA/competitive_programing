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
        input = """4 3
1 2 1 3
1 3
2 4
3 3"""
        output = """2
3
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 10
2 5 6 5 2 1 7 9 7 2
5 5
2 4
6 7
2 2
7 8
7 9
1 8
6 9
8 10
6 8"""
        output = """1
2
2
1
2
2
6
3
3
3"""
        self.assertIO(input, output)

class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
          self.data[i] += x
          i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

def resolve():
  N, Q = map(int, input().split(" "))
  C = [int(x)-1 for x in input().split(" ")]
  QUERY = sorted([(i, *[int(x) for x in input().split(" ")]) for i in range(Q)], key=lambda x: x[2])

  BITree = BIT(N)
  right_end = [-1]*N
  ans = [0]*Q
  current_r = 0
  for i, l, r in QUERY:
    for r_ in range(current_r+1, r+1):
      c = C[r_-1]
      if right_end[c] >= 0:
        BITree.add(right_end[c], -1)
      right_end[c] = r_
      BITree.add(right_end[c], 1)
    current_r = r
    ans[i] = BITree.get(l-1, r)
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
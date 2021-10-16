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
        input = """6
0 0
0 1
1 0
1 1
2 0
2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
0 1
1 2
2 3
3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
0 1
1 0
2 0
2 1
2 2
3 0
3 2"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # x, y で集計する。
  from collections import defaultdict
  from itertools import combinations

  agg_x = defaultdict(set)
  agg_y = defaultdict(set)

  N = int(input())
  for _ in range(N):
    x, y = map(int, input().split(" "))
    agg_x[x].add(y)
    agg_y[y].add(y)

  # print(agg_x, )
  ans = 0
  target_x = agg_x.keys()
  for x1, x2 in combinations(target_x, 2):
    target_y = list(agg_x[x1])
    for y1, y2 in combinations(target_y, 2):
      if y1 in agg_x[x2] and y2 in agg_x[x2]:
        ans+=1
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
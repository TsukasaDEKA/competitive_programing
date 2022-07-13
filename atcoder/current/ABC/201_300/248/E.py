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
        input = """5 2
0 0
1 0
0 1
-1 0
0 -1"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 1
0 0"""
        output = """Infinity"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  from collections import defaultdict
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  X_Y = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])

  min_x = -10**18
  min_y = -10**18
  for i in range(N):
    x_s, y_s = X_Y[i]
    min_x = min(min_x, x_s)
    min_y = min(min_y, y_s)
  
  X_Y = [[x-min_x, y-min_y] for x, y in X_Y]
  if K == 1:
    print("Infinity")
    return

  # 使用したもの
  used = set()
  ans = 0
  for i in range(N-1):
    # 元の点を i 番目の点に定める。
    x_s, y_s = X_Y[i]
    target = defaultdict(list)
    for j in range(i+1, N):
      # 二番目の点を j 番目の点に定める。
      x_n, y_n = X_Y[j]

      x_diff = x_n-x_s
      y_diff = y_n-y_s

      # 最小公倍数を求める。
      if x_diff == 0: y_diff = 1
      if y_diff == 0: x_diff = 1
      g = gcd(x_diff, y_diff)
      x_diff //= g
      y_diff //= g

      if (x_diff, y_diff, j) in used: continue
      target[(x_diff, y_diff)].append(j)

    # print(i, target)
    for key, val in target.items():
      x_diff, y_diff = key
      if len(val) >= K-1:
        ans+=1

      for v in val:
        used.add((x_diff, y_diff, v))

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
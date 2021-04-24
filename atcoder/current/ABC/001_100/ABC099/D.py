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
        input = """2 3
0 1 1
1 0 1
1 4 0
1 2
3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3
0 12 71
81 0 53
14 92 0
1 1 2 1
2 1 1 2
2 2 1 3
1 1 2 2"""
        output = """428"""
        self.assertIO(input, output)

def resolve():
  # N <= 500 なので最大 250000 マス
  # 斜め or 3 本跨ぎで同じ色になる必要がある。
  # 3色しか使わないので、同色になるマスで集計をとると楽そう。
  # C が 30 までなので、全探索で間に合うかも？
  # 最大30*29*28*3*30 = 2192400 なので。
  from collections import defaultdict
  from itertools import permutations

  inf = 10**18+1
  N, M = map(int, input().split(" "))
  D = [list(map(int, input().split(" "))) for _ in range(M)]
  C = [[int(x)-1 for x in input().split(" ")] for _ in range(N)]
  agg = [defaultdict(int) for _ in range(3)]

  for i in range(N):
    for j in range(N):
      agg[(i+j)%3][C[i][j]]+=1

  ans = inf
  for pattarn in permutations(list(range(M)), 3):
    temp = 0
    for i in range(3):
      tar = pattarn[i]
      for c, v in agg[i].items():
        temp+=v*D[c][tar]
    ans = min(ans, temp)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

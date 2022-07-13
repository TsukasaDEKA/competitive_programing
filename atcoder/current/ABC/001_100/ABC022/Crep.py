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
        input = """5 7
1 2 2
1 4 1
2 3 7
1 5 12
3 5 2
2 5 3
3 4 5"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4
1 2 1
1 3 1
1 4 1
1 5 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 12
1 4 3
1 9 1
2 5 4
2 6 1
3 7 5
3 10 9
4 7 2
5 6 6
5 8 5
6 8 3
7 9 5
8 10 8"""
        output = """11"""
        self.assertIO(input, output)

def resolve():
  # 道は双方向。
  # N の数は小さい。
  # 1 に繫がる道の内、どれか２本は絶対に使用する必要がある。
  # 1 を経由しない 1 の隣接頂点間の最短距離を求めて、
  # その内 2 頂点間の距離と、1 とその頂点 2 個との距離を足した距離が最も小さい組み合わせを見つける。
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  EDGES = [[inf]*N for _ in range(N)]
  for i in range(M):
    u, v, l = [int(x) for x in input().split(" ")]
    u, v = u-1, v-1
    EDGES[u][v] = EDGES[v][u] = l

  # 始点、終点、経由点として 1 を選ばない状態でそれぞれの最短距離を求める。
  for k in range(1, N):
    for j in range(1, N):
      for i in range(1, N):
        if j == i: continue
        EDGES[i][j] = EDGES[j][i] = min(EDGES[i][j], EDGES[i][k]+EDGES[j][k])
  ans = inf
  for i in range(1, N-1):
    for j in range(i+1, N):
      ans = min(ans, EDGES[0][i] + EDGES[0][j] + EDGES[i][j])
  print(ans if ans < inf else -1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
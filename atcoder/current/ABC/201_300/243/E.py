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
        input = """3 3
1 2 2
2 3 3
1 3 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4
1 3 3
2 3 9
3 5 3
4 5 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 10
1 2 71
1 3 9
1 4 82
1 5 64
2 3 22
2 4 99
2 5 1
3 4 24
3 5 18
4 5 10"""
        output = """5"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  EDGES = [[int(x) for x in input().split(" ")] for _ in range(M)]
  diff = [[inf]*N for _ in range(N)]

  # 初期値を保存しておく。
  initial = [[inf+1]*N for _ in range(N)]
  for i in range(M):
    a, b, c = EDGES[i]
    a, b = a-1, b-1
    diff[a][b] = diff[b][a] = c
    initial[a][b] = initial[b][a] = c

  # ワーシャルフロイドで 2 点間の距離を求める。
  # 区間更新が初めて入ったタイミングで特定の頂点を直接繋いでいる辺を使わなくてもいいことがわかる。
  ans = set()
  for k in range(N):#経由点
    for i in range(N):#始点
      for j in range(i+1, N):#終点
        if diff[j][i] < diff[i][k]+diff[k][j]: continue
        if diff[j][i] == initial[i][j]: ans.add((i, j))
        diff[i][j] = diff[j][i] = diff[i][k]+diff[k][j]

  print(len(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
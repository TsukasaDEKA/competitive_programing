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
        input = """2 4
0 9 9 9 9 9 9 9 9 9
9 0 9 9 9 9 9 9 9 9
9 9 0 9 9 9 9 9 9 9
9 9 9 0 9 9 9 9 9 9
9 9 9 9 0 9 9 9 9 2
9 9 9 9 9 0 9 9 9 9
9 9 9 9 9 9 0 9 9 9
9 9 9 9 9 9 9 0 9 9
9 9 9 9 2 9 9 9 0 9
9 2 9 9 9 9 9 9 9 0
-1 -1 -1 -1
8 1 1 8"""
        output = """12"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
0 999 999 999 999 999 999 999 999 999
999 0 999 999 999 999 999 999 999 999
999 999 0 999 999 999 999 999 999 999
999 999 999 0 999 999 999 999 999 999
999 999 999 999 0 999 999 999 999 999
999 999 999 999 999 0 999 999 999 999
999 999 999 999 999 999 0 999 999 999
999 999 999 999 999 999 999 0 999 999
999 999 999 999 999 999 999 999 0 999
999 999 999 999 999 999 999 999 999 0
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 5
0 4 3 6 2 7 2 5 3 3
4 0 5 3 7 5 3 7 2 7
5 7 0 7 2 9 3 2 9 1
3 6 2 0 2 4 6 4 2 3
3 5 7 4 0 6 9 7 6 7
9 8 5 2 2 0 4 7 6 5
5 4 6 3 2 3 0 5 4 3
3 6 2 3 4 2 4 0 8 9
4 6 5 4 3 5 3 2 0 8
2 1 3 4 5 7 8 6 4 0
3 5 2 6 1
2 5 3 2 1
6 9 2 5 6"""
        output = """47"""
        self.assertIO(input, output)

def resolve():
  # DP を使って任意の数字を 1 に変換する時の最小魔力を求めて、あとはその表に照らし合わせて魔力の合計値を求める。
  # 計算量は最小変換魔力表作成に 10**3、合計値算出に 4*10**4 なので間に合いそう。
  inf = 10**10+1
  H, W = map(int, input().split(" "))
  cost = [[int(x) for x in input().split(" ")] for _ in range(10)]
  wall = [[int(x) for x in input().split(" ")] for _ in range(H)]
  dp = [[inf]*10 for _ in range(10)]

  # 該当する番号から 1 に変換する時の最小魔力を計算する。
  for i in range(10):
    dp[0][i] = cost[i][1]
  for i in range(1, 10):
    is_updated = False
    for j in range(10):
      for k in range(10):
        dp[i][j] = min(dp[i-1][k]+cost[j][k], dp[i][j])
      if dp[i-1][j] != dp[i][j]:is_updated=True
    if not is_updated:
      cost = dp[i]
      break
  # cost = dp[-1]

  ans = 0
  for i in range(H):
    for j in range(W):
      if wall[i][j] != -1:
        ans+=cost[wall[i][j]]
  print(ans)
resolve()

if __name__ == "__main__":
    unittest.main()

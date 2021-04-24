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
        input = """3
0.30 0.60 0.80"""
        output = """0.612"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
0.50"""
        output = """0.5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5
0.42 0.01 0.42 0.99 0.42"""
        output = """0.3821815872"""
        self.assertIO(input, output)

def resolve():
  # 解説: https://kyopro-friends.hatenablog.com/entry/2019/01/12/231000
  # dp[i][j] = 
  # (i−1枚目のコインまで投げたとき、表がj枚でる確率)×(i枚目のコインが裏である確率)
  # +(i−1枚目のコインまで投げたとき、表がj−1枚でる確率)×(i枚目のコインが表である確率)
  # 1-index でやる (j 枚出る、i 枚目、とかインデックス操作するのがしんどいので。)
  N = int(input())
  # インデックス調整で先頭に 0.0 を入れる。
  P = [0.0]+[float(x) for x in input().split(" ")]
  dp = [[0.0]*(N+1) for _ in range(N+1)]
  dp[0][0] = 1.0
  for i in range(1, N+1):
    for j in range(i+1):
      if j == 0:
        # 全てが裏の確率 = i-1 枚目まで全て裏の確率 * i 枚目が
        dp[i][j] = dp[i-1][j]*(1-P[i])
        continue
      dp[i][j] = dp[i-1][j]*(1-P[i]) + dp[i-1][j-1]*P[i]
  print(*dp, sep="\n")
  print(sum(dp[-1][(N+1)//2:]))

# resolve()

if __name__ == "__main__":
    unittest.main()

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
        input = """3 3
---
+-+
+--"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 4
+++-
-+-+"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 1
-"""
        output = """Draw"""
        self.assertIO(input, output)

def resolve():
  # 操作回数は H+W-1。
  # 全探索すると 2**(H+W-1) の計算をすることになる。
  # 右下から DP していく
  # h+w が偶数だったら青木くんのスコア
  # h+w が奇数だったら高橋くんのスコア
  # スコアを T-S だとすると、青木くんはスコアの最小化、高橋くんは最大化を目指す。
  inf = 10**9+1
  H, W = map(int, input().split(" "))
  A = [[x=="+" for x in list(input())] for _ in range(H)]

  if H==1 and W == 1: 
    print("Draw")
    return

  dp = [[0]*W for _ in range(H)]
  dp[-1][-1] += 1 if A[-1][-1] else -1
  if (H+W)%2 == 0:
    dp[-1][-1] *= -1

  for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
      if h == H-1 and w == W-1: continue
      # 高橋くんがとるマス
      if (h+w)%2:
        tar = inf
        if h+1 < H: tar = min(tar, dp[h+1][w])
        if w+1 < W: tar = min(tar, dp[h][w+1])
        dp[h][w] = tar+1 if A[h][w] else tar-1
      else:
        tar = -inf
        if h+1 < H: tar = max(tar, dp[h+1][w])
        if w+1 < W: tar = max(tar, dp[h][w+1])
        dp[h][w] = tar-1 if A[h][w] else tar+1

  # print(*dp, sep="\n")
  ans = -inf
  if 1 < H: ans = max(ans, dp[1][0])
  if 1 < W: ans = max(ans, dp[0][1])
  if ans == 0:
    print("Draw")
  elif ans > 0:
    print("Takahashi")
  else:
    print("Aoki")

import sys
if sys.argv[-1] == './Main.py':
  resolve()


if __name__ == "__main__":
    unittest.main()

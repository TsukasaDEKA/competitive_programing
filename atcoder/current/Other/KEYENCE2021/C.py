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
        input = """2 2 3
1 1 X
2 1 R
2 2 R"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 5
2 3 D
1 3 D
2 1 D
1 2 X
3 1 R"""
        output = """150"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """5000 5000 10
# 585 1323 R
# 2633 3788 X
# 1222 4989 D
# 1456 4841 X
# 2115 3191 R
# 2120 4450 X
# 4325 2864 X
# 222 3205 D
# 2134 2388 X
# 2262 3565 R"""
#         output = """139923295"""
#         self.assertIO(input, output)

def resolve():
  # DP なんだけど非常に厄介。
  # ある空白マスを通る場合 => そのマスが R, D, X それぞれの場合を計算すれば良い。
  # ある空白マスを通らない場合 => それ以外の経路について、3^<空白マスの個数> 分のバリエーションが生まれる。
  mod = 998244353
  H, W, K = map(int, input().split(" "))
  MAP = [[None]*W for _ in range(H)]
  for _ in range(K):
    h, w, c = input().split(" ")
    h = int(h)-1
    w = int(w)-1
    MAP[h][w] = c
  
  dp = [[0]*W for _ in range(H)]
  dp[0][0] = 1
  for h in range(H):
    for w in range(W):
      if h == 0 and w == 0: continue
      
      left = 0
      if w-1 >= 0:
        if MAP[h][w-1] is None:
          left = dp[h][w-1]*2
        if MAP[h][w-1] == "R" or MAP[h][w-1] == "X":
          left = dp[h][w-1]
      up = 0
      if h-1 >= 0:
        if MAP[h-1][w] is None:
          up = dp[h-1][w]*2
        if MAP[h-1][w] == "D" or MAP[h-1][w] == "X":
          up = dp[h-1][w]
      dp[h][w] = left + up
  print(*MAP, sep="\n")
  print(*dp, sep="\n")
  print(dp[-1][-1]%mod)

# resolve()

if __name__ == "__main__":
    unittest.main()

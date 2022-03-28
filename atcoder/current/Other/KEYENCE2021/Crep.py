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
  mod = 998244353
  # 左と上を見てそこから遷移すると考える。
  # 通らなかったマス * 3 倍を掛けたい
  # => 通ったら 3 で割って、最終的に 3*(H*W-K) をかければ良さそう。
  H, W, K = map(int, input().split(" "))
  dp = [0]*W
  dp[0] = 1
  to_int = {"R": 1, "D": 2, "X": 3}
  FIELD = [[0]*W+[to_int["D"]] for _ in range(H)]+[[to_int["R"]]*(W+1)]
 
  for _ in range(K):
    h, w, c = input().split(" ")
    h, w = int(h)-1, int(w)-1
    FIELD[h][w] = to_int[c]
 
  D = to_int["D"]
  R = to_int["R"]
  per23 = (2*pow(3, mod-2, mod))%mod
  temp = dp
  for h in range(H):
    for w in range(W):
      if h == 0 and w == 0: continue
      up = FIELD[h-1][w]
      if up == 0: temp[w] += (dp[w]*per23)%mod
      elif up & D: temp[w] += dp[w]
 
      left = FIELD[h][w-1]
      if left == 0: temp[w] += (temp[w-1]*per23)%mod
      elif left & R: temp[w] += temp[w-1]
 
      if temp[w] >= mod: temp[w]%=mod
    dp = temp
    temp = [0]*W
  dp[-1]%=mod
  print((dp[-1]*pow(3, H*W-K, mod))%mod)
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
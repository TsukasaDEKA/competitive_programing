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
        input = """2 60
10 10
100 100"""
        output = """110"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 60
10 10
10 20
10 30"""
        output = """60"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 60
30 10
30 20
30 30"""
        output = """50"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 100
13 17
15 23
18 20
18 29
19 27
20 18
22 25
23 21
24 12
27 15"""
        output = """145"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """9 100
# 13 17
# 15 23
# 18 29
# 19 27
# 20 18
# 22 25
# 23 21
# 24 12
# 27 15"""
#         output = """145"""
#         self.assertIO(input, output)

def resolve():
  # DP だけどラストオーダーだけが決まってて、食べ終わる時間はいつでもいいのがネック
  # i 番目の皿を最後に注文するとき、Ai を 1 として扱って良い。
  # Ai を 1 として扱った場合、それ以上の料理を食べることができない。
  # Ai を 1 として扱う場合とそうでない場合で分離して考えれば良さそう。
  # i 以下の皿の中で最も大きな Ai を 1 として扱う方がお得。
  # なので、Ai で昇順ソートしておく。
  # dp[t] = t 秒以下での美味しさの総和の最大値
  N, T = map(int, input().split(" "))
  DISHES = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])
  dp = [-1]*(T+1)
  dp[0] = 0
  for i in range(N):
    temp_dp = [-1]*(T+1)
    temp_dp[0] = 0
    A, B = DISHES[i]
    for t in range(T):
      if dp[t] < 0: continue
 
      temp_dp[min(T, A+t)] = max(temp_dp[min(T, A+t)], dp[min(T, A+t)], dp[t]+B)
      temp_dp[t] = max(temp_dp[t], dp[t])
    # print(A, B)
    # print(*dp)
    # print(*temp_dp)
    dp = temp_dp

  print(max(dp))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
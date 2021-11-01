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
        input = """??2??5"""
        output = """768"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """?44"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7?4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???"""
        output = """153716888"""
        self.assertIO(input, output)

def resolve():
  # dp でいけそう。
  # dp[i][j] = i 桁目まで見た時、13 で割った余りが j になる場合数とし、これを解く。
  # 計算量的には N*10*13 < 10**8でいけそうなんんだけど TLE する。
  # アクセスが遅い？高速化を考える。
  # 一次元配列を入れ替える方式でやってみる。
  # => 遅かった
  from itertools import accumulate # 累積和作るやつ

  mod = 10**9+7
  range_10= list(range(10))
  range_13= list(range(13))

  S = list(input())
  N = len(S)
  dp = [0]*13
  if S[0] == "?":
    for j in range_10: dp[j] = 1
  else:
    dp[int(S[0])] = 1

  for i in range(1, N):
    temp_dp = [0]*13
    if S[i] == "?":
      for j in range_13:
        for k in range_10:
          temp_dp[(j*10+k)%13] += dp[j]
    else:
      for j in range_13:
        temp_dp[(j*10+int(S[i]))%13] = dp[j]

    for j in range_13:
      if temp_dp[j] >= mod: temp_dp[j]%=mod
    dp = temp_dp
  print(dp[5])
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

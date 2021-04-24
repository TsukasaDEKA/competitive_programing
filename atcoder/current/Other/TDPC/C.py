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
        input = """1
2200
2600"""
        output = """0.090909091
0.909090909"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
2000
2500
2300
2700
2100
2400
2600
2200"""
        output = """0.000086893
0.122042976
0.005522752
0.493464665
0.000651695
0.053982389
0.321828438
0.002420190"""
        self.assertIO(input, output)

def resolve():
  # K <= 10 なので、参加人数はせいぜい 1024 程度。小さい。
  # 一回戦目で人0 が勝つ確率は 1/(1+10**((R0-R1)/400)) になる。
  # 二回戦目で人0 が勝つ確率は (一回戦で人0 が勝つ確率) * (1/(1+10**((R0-R2)/400)) (人2が一回戦で勝つ確率) + 1/(1+10**((R0-R3)/400)) (人3が一回戦で勝つ確率))(= この試合で 0 が勝つ確率)
  # 繰り返していくと、N=2**K として O(N*N*log(N)) の計算量・・・多分
  # 上手く式変形して O(N*log(N)) くらいまで落とせるかも？
  # dp[i][j] = i 回戦目で j さんが勝つ確率
  # メモ化再帰で実装？とりあえずループで書いてみる。
  K = int(input())
  R = [int(input()) for _ in range(2**K)]

  dp = [[1]*(2**K) for _ in range(K+1)]

  def winning_rate(player_rate, opponent_rate):
    return 1/(1+10**((opponent_rate-player_rate)/400))

  # 1 ~ K 回戦まで計算する。
  for i in range(1, K+1):
    for j in range(2**K):
      # 区間設定がめんどい。
      step = 2**(i-1)
      left = j - (j%step) - step if j//(2**(i-1))%2 else j - (j%step) + step
      # 半開区間で扱った方が楽？
      right = left + step

      temp_rate = 0
      for k in range(left, right):
        temp_rate += winning_rate(R[j], R[k])*dp[i-1][k]
      dp[i][j] = dp[i-1][j]*temp_rate

  for i in range(2**K):
    print("{:.9f}".format(dp[K][i]))

resolve()

if __name__ == "__main__":
    unittest.main()

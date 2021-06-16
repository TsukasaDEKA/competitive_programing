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

    def test_入力例_1(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """234"""
        output = """757186539"""
        self.assertIO(input, output)

    # def test_入力例_3(self):
    #     input = """9"""
    #     output = """0"""
    #     self.assertIO(input, output)

def resolve():
  # 「X を 10 進法で表したときの各桁の数字の和は K」を満たすなら「X は 9 の倍数」である。
  # K 個のボールを並べて、1 個以上、9 個以下で分割する方法がいくつあるか考える。
  # 9 個のボールの組みが K//9 個あると考える？
  # K = 18 の時、828 とか 8118 とかあるので、
  # 組みと組みの間に境を置くかどうかも考えなきゃいけないし、
  # おかなかった場合に 9 を超えないかどうかも考える必要がある。
  # DP で考えてみる。
  # 合計が 1 になる組み合わせは 1 パターン
  # 合計が 2 になる組み合わせは 11, 2 の 2 パターン
  # 合計が 3 になる組み合わせは 12 111 21 3 の 4 パターン
  # 合計が 4 になる組み合わせは 13 の 1 + 112, 22 + 121 1111 211 31 の 4 パターン + 
  # 合計が X になる組み合わせは、X-9, X-8・・・X-1 のパターンをそれぞれ足して、それに +1 すれば良さそう。
  mod = 10**9+7
  K = int(input())
  if K%9:
    print(0)
    return

  dp = [0]*(K+1)
  dp[0] = 1
  for i in range(1, K+1):
    for j in range(max(0, i-9), i):
      dp[i] += dp[j]
      if dp[i]>=mod: dp[i]%=mod
  print(dp[-1]%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

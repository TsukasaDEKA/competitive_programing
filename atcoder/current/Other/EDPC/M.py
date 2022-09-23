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
        input = """3 4
1 2 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 10
9"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 0
0 0"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4 100000
100000 100000 100000 100000"""
        output = """665683269"""
        self.assertIO(input, output)

def resolve():
  # N <= 100, K<=10**5
  mod = 10**9 + 7
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  # i 番目の子供まで配った時の合計値で DP ?
  # 余ってはいけないという条件が厳し目。
  # 再帰的に解いていくか。
  # 累積和を取っておくと、余らない配り方はすぐ出せる。
  # 最後の一人 (N番目の人) には残った全ての飴を渡さなきゃいけない。
  # N番目の人だけ自明
  # N-1 番目の人がとりうる値について考えてみる。
  # N-1 番目の人に渡す数が少ないと、N 番目の人に飴を配りきれないかもしれない。
  # なので、max(K-(今まで配った個数)-A[N], 0) より多くなきゃいけない
  # 当然 A[N-1] 未満じゃなきゃいけない。
  # だんだんと計算量が増えていきそうなので、別の考え方でやってみる。

  # 配る DP でできそうなのでやってみる。計算量が怪しい。
  # 配る DP だと例4 の段階で結構な時間がかかっている。
  # 高速化をする。
  # ループの最後でやってる dp[i+1][k] は sum(dp[i][max(0, j-A[i+1]):j+1]) なので、ここだけ累積和をする。

  # accumulate すると Python でも間に合うらしい。
  from itertools import accumulate
  dp = [[0]*(K+1) for _ in range(N)]

  # 初期化
  for i in range(K-A[0], K+1):
    dp[0][i] = 1

  for i in range(1, N):
    integral = [0]*(K+2)
    integral[1:] = accumulate(dp[i-1])
    for j in range(K+1):
      dp[i][j] = integral[min(K+1, j+A[i]+1)] - integral[j]
      if dp[i][j] > mod or dp[i][j] < mod: dp[i][j]%=mod
  print(dp[-1][0])

# resolve()

if __name__ == "__main__":
    unittest.main()

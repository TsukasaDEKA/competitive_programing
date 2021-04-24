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

#     def test_Sample_Input_1(self):
#         input = """3
# 1 1 1"""
#         output = """5.5"""
#         self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """1
# 3"""
#         output = """3"""
#         self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2
1 2"""
        output = """4.5"""
        self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """10
# 1 3 2 3 3 2 3 2 1 3"""
#         output = """54.48064457488221"""
#         self.assertIO(input, output)


# def solve(i, j, k, dp, checked, N):
#   if checked[i][j][k]: return dp[i][j][k]
#   checked[i][j][k] = True
#   dp[i][j][k] = N
#   if i>0: dp[i][j][k]+=solve(i-1,   j, k, dp, checked, N)*i
#   if j>0: dp[i][j][k]+=solve(i+1, j-1, k, dp, checked, N)*j
#   if k>0: dp[i][j][k]+=solve(i, j+1, k-1, dp, checked, N)*k
#   dp[i][j][k] /= i+j+k
#   return dp[i][j][k]

def resolve():
  # 参考 : https://compro.tsutaj.com//archive/180220_probability_dp.pdf  https://drken1215.hatenablog.com/entry/2019/03/23/214500、https://mathtrain.jp/completegacha
  # 操作回数の期待値を DP にする。
  # 単純なサイコロ問題から解いた方が良さそう。
  # 例 1 は典型的なコンプガチャ。3*(1 + 1/2 + 1/3) = 5.5
  # 例 2 は成功確率 1.0 が 3 回なので 3.0。
  # 例 3 : A = [1, 2] の場合を考える。

  # 0 個の皿が選ばれる確率を考慮してなかった。
  # dp[i][j][k] = 1 + dp[i-1][j][k]*(i/N) + dp[i+1][j-1][k]*(j/N) + dp[i][j+1][k-1]*(k/N) + dp[i][j][k]*((N-i-j-k)/N)
  # N*dp[i][j][k] = N + dp[i-1][j][k]*i + dp[i+1][j-1][k]*j + dp[i][j+1][k-1]*k + dp[i][j][k]*(N-i-j-k)
  # (N - (N-i-j-k))*dp[i][j][k] = N + dp[i-1][j][k]*i + dp[i+1][j-1][k]*j + dp[i][j+1][k-1]*k
  # (i+j+k)*dp[i][j][k] = N + dp[i-1][j][k]*i + dp[i+1][j-1][k]*j + dp[i][j+1][k-1]*k

  N = int(input())
  SUSHI = list(map(int, input().split(" ")))
  count = [0, 0, 0, 0]
  for sushi in SUSHI: count[sushi]+=1


  dp = [[[0.0]*(N+2) for _ in range(N+2)] for _ in range(N+2)]
  # checked = [[[False]*(N+2) for _ in range(N+2)] for _ in range(N+2)]
  # dp に入るのは「各皿が i, j, k 枚の時に全て食べ切るまでの操作回数の期待値」なので、dp[0][0][0] = 0 で確定
  # checked[0][0][0] = True
  # print(*count[1:], dp, checked)

  # dp で k インデックス　( 1 個の皿を取る確率 ) が先行的に参照されるので、そちらのループを先に回す必要がある。
  # j も i より先行するものの、i == 0 の時は参照されても i*dp[i-1][j+1][k] の項が 0 になるので問題ないはず。
  # i の範囲は、最初に求めた 0 ~ 3個の皿の個数になる。(単調に減っていくので)
  # j の範囲は、N - (最初に求めた1個の皿) - (計算時の3個の皿)
  # k の範囲は、計算時の N - (2個の皿) - (3個の皿)
  for i in range(count[3]+1):
    for j in range(N-count[1]-i+1):
      for k in range(N-i-j+1):
        if i+j+k: dp[i][j][k] = (N + i*dp[i-1][j+1][k] + j*dp[i][j-1][k+1] + k*dp[i][j][k-1])/(i+j+k)
  # for p in dp:
  #   print()
  #   print(*p, sep="\n")
  print(dp[count[3]][count[2]][count[1]])
  # print(dp)

resolve()

if __name__ == "__main__":
    unittest.main()

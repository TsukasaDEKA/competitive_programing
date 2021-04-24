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

    # def test_Sample_Input_1(self):
    #     input = """10 1"""
    #     output = """15"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """FF 2"""
    #     output = """225"""
    #     self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 2"""
        output = """226"""
        self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """1A8FD02 4"""
    #     output = """3784674"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_5(self):
    #     input = """DEADBEEFDEADBEEEEEEEEF 16"""
    #     output = """153954073"""
    #     self.assertIO(input, output)

def resolve():
  # N がやばいくらい多い
  # 2*10**5 桁
  # K は 16 種類以下
  mod = 10**9+7
  N, K = input().split(" ")

  K = int(K)
  # 解説 AC 防止
  if K == 16: return;
  N = [int(x, 16) for x in list(N)]
  # K 桁の数字を使って、全て計算して、 N 以下のものを数える。
  # 例えば N= 24* だとしたら、1[2-9], 2[1~4] の組み合わせになる。
  # 例えば N = 32* だとしたら、1[0,2-F=>(16-1)種類], 2[0-1,3-F=>(16-1)種類], 3[0-3(A[1]+1種類)] の組み合わせになる。
  # なので、dp[2][2] = ((dp[1][1]-1)*15+(A[1]+1)) になる。
  # 一般化する際は dp[1][2] も考慮した方が良さそう。
  # j が既に選択した数字の個数で、それの内からどれかを選ぶ事になるので、
  # dp[2][2] = ((dp[1][1]-1)*15+(A[1]+1)) + dp[1][2]
  # 一般化すると dp[i][j] = dp[i-1][j-1]*15 + (A[i]+1)
  dp = [[0]*(K+1+1) for _ in range(len(N)+1)]
  dp[1][1] = N[0]
  # 初期化

  for i in range(1,len(N)):
    for j in range(min(K, i)+1):
      # i+1 桁目を追加した時に数字の種類が増えない。(今まで出てきた数字と同じものが出た場合)
      # dp[i+1][j] += max(dp[i][j]-1, 0)*j + min(j, )
      # i+1 桁目を追加した時に数字の種類が増える。(今まで出てきた数字と違うものが出た場合)
      if j == 0:
        dp[i+1][j+1] += 15
      else:
        dp[i+1][j+1] += (dp[i][j]-1) * (16-j+1) + N[i] + 1
      print("", *dp, sep="\n")
  print(dp[len(N)][K])
# resolve()

if __name__ == "__main__":
    unittest.main()

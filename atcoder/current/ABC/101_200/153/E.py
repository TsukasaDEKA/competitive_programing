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
        input = """9 3
8 3
4 2
2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100 6
1 1
2 3
3 9
4 27
5 81
6 243"""
        output = """100"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """9999 10
# 540 7550
# 691 9680
# 700 9790
# 510 7150
# 415 5818
# 551 7712
# 587 8227
# 619 8671
# 588 8228
# 176 2461"""
#         output = """139815"""
#         self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  # 個数制限無し DP 
  # DP サイズは 10**7 なので足りそう。
  H, N = map(int, input().split(" "))

  dp = [[inf]*(H+1) for _ in range(N+1)]
  # dp[i][j] = i 番目までの呪文からダメージの総和が j 以上になるように選んだ時の魔力の最小値
  for i in range(N):
    A, B = [int(x) for x in input().split(" ")]
    for j in range(H+1):
      temp_mp = dp[i+1][j-A] if j-A >= 0 else 0
      dp[i+1][j] = min(dp[i][j], temp_mp+B)
  print(dp[N][-2])

resolve()

if __name__ == "__main__":
    unittest.main()

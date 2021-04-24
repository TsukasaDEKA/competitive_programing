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
        input = """4 3
1 2 1 3
1 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 6
1 3 2 4
1 5 2 6 4 3"""
        output = """3"""
        self.assertIO(input, output)


    def test_Sample_Input_3(self):
        input = """7 4
1 4 3 2 3 4 8
1 3 2 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 5
1 1 1 1 1
1 1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N, M = map(int, input().split(" "))
  A = [x for x in input().split(" ")]
  B = [x for x in input().split(" ")]
  dp = [[0]*(M+1) for _ in range(N+1)]

  for n in range(N+1):
    for m in range(M+1):
      if n==0 or m==0:
        # 片方が 0 ならもう片方を全部取り除く
        dp[n][m] = max(n, m)
        continue

      # 0-index なので合わせるために -1 してる。
      if A[n-1]==B[m-1]:
        # Ai と Bj が一致している場合には取り除く必要がないので 0
        add = 0
      else:
        add = 1
      # 例えば A = 1, B= 3 1 で n = 1, m = 2 の時に、
      # dp[1][1]+1 = 1+1 = 2、
      # dp[0][2]+1 = 2+1 = 3、 
      # dp[0][1]+0 = 1 なので 
      # dp[1][2] = 1 になる。
      dp[n][m] = min(dp[n][m-1]+1, dp[n-1][m]+1, dp[n-1][m-1]+add)

  # print(*dp, sep="\n")
  print(dp[N][M])

resolve()

if __name__ == "__main__":
    unittest.main()

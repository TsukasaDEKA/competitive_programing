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
        input = """4 2"""
        output = """2"""
        self.assertIO(input, output)

    # def test_Sample_Input_1(self):
    #     input = """10 8"""
    #     output = """2"""
    #     self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2525 425"""
        output = """687232272"""
        self.assertIO(input, output)

def resolve():
  mod = 998244353
  N, K = map(int, input().split(" "))

  # dp = [[0]*(K+1) for _ in range(N+1)]
  dp = [[0]*(N+1) for _ in range(N+1)]
  for n in range(N+1):
    dp[n][n] = 1

  for n in range(1, N+1):
    for k in range(n, 0, -1):
      result = dp[n-1][k-1]
      if 2*k <= n: result += dp[n][2*k]
      dp[n][k] = result%mod if result > mod else result
  
  print(dp[N][K])

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()

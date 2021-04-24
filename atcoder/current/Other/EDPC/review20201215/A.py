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
        input = """4
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)


def resolve():
  # もらっていく DP
  # i の足場に行くまでのコストを出していく。
  # dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))。
  inf = 10**10+1
  N = int(input())
  H = [int(x) for x in input().split(" ")]

  dp = [0]*N
  dp[1] = abs(H[1]-H[0])
  for i in range(2, N):
    dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))
  print(dp[-1])

resolve()

if __name__ == "__main__":
    unittest.main()

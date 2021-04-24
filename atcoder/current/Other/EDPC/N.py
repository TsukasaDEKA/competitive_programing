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
        input = """4
10 20 30 40"""
        output = """190"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
10 10 10 10 10"""
        output = """120"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1000000000 1000000000 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
7 6 8 6 1 1"""
        output = """68"""
        self.assertIO(input, output)

def resolve():
  from itertools import accumulate # 累積和作るやつ
  inf = 10**18+1

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  integral = [0] + list(accumulate(A))
  dp = [[0]*N for _ in range(N)]
  K = [[0]*N for _ in range(N)]
  for i in range(1, N):
    K[i][i] = i-1

  for j in range(1, N):
    for i in range(N-j):
      l = i
      r = i+j
      temp = inf
      for k in range(K[i][i+j-1], K[i+1][i+j]+1):
        t = dp[l][k] + dp[k+1][r]
        if t <= temp:
          temp = t
          K[l][r] = k
      dp[i][i+j] = integral[r+1] - integral[l] + temp


  print(dp[0][-1])

resolve()

if __name__ == "__main__":
    unittest.main()

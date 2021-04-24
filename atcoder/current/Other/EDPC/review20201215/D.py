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
        input = """3 8
3 30
4 50
5 60"""
        output = """90"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)

def resolve():
  # ナップザック問題
  # dp の値は価値の総和の最大値
  # dp[i][w] とすると、i は 0 ~ i 番目の品物で w は重さの最大値
  # dp[0][w]、dp[i][0] = 0
  inf = 10**10+1
  N, W = map(int, input().split(" "))
  dp = [0]*(W+1)

  for i in range(1, N+1):
    w, v = map(int, input().split(" "))
    for w_ in reversed(range(w, W+1)):
      dp[w_] = max(dp[w_-w]+v, dp[w_]) 
  # print(*dp, sep="\n")
  print(dp[-1])

resolve()

if __name__ == "__main__":
    unittest.main()

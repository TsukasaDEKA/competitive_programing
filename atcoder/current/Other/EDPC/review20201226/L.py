# https://atcoder.jp/contests/dp/tasks/dp_l
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
10 80 90 30"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
10 100 10"""
        output = """-80"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
10"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10
1000000000 1 1000000000 1 1000000000 1 1000000000 1 1000000000 1"""
        output = """4999999995"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """6
4 2 9 7 1 5"""
        output = """2"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = tuple(map(int, input().split(" ")))

  dp = [[0]*(N+1) for _ in range(N+1)]
  for i in range(N+1, -1, -1):
    for j in range(i+1, N+1): dp[i][j] = max(A[i] - dp[i+1][j], A[j-1] - dp[i][j-1])
  print(dp[0][N])
resolve()

if __name__ == "__main__":
    unittest.main()

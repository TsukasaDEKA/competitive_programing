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
        input = """3
10 40 70
20 50 80
30 60 90"""
        output = """210"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
100 10 1"""
        output = """100"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1"""
        output = """46"""
        self.assertIO(input, output)

def resolve():
  N = int(input())

  dp = [[0]*3 for _ in range(N)]

  # 初日
  dp[0] = [int(x) for x in input().split(" ")]

  for i in range(1, N):
    happiness_list = [int(x) for x in input().split(" ")]
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) +  happiness_list[0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) +  happiness_list[1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) +  happiness_list[2]
  print(max(*dp[-1]))

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()

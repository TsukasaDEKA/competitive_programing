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
  inf = 10**10+1
  # 二次元 DP
  N = int(input())
  dp = [[0]*3 for _ in range(N)]
  for i in range(N):
    A, B, C = map(int, input().split(" "))
    if i == 0:
      dp[0] = [A, B, C]
      continue
    A_, B_, C_ = dp[i-1]
    dp[i][0] = A+max(B_, C_)
    dp[i][1] = B+max(A_, C_)
    dp[i][2] = C+max(A_, B_)
  # print(*dp, sep="\n")
  print(max(*dp[-1]))
resolve()

if __name__ == "__main__":
    unittest.main()

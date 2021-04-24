import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    maxDiff=None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """99 99 99"""
        output = """1.000000000"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """98 99 99"""
    #     output = """1.331081081"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """0 0 1"""
    #     output = """99.000000000"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """31 41 59"""
    #     output = """91.835008202"""
    #     self.assertIO(input, output)

def resolve():
  A, B, C = map(int, input().split(" "))
  N=3
  dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
  for i in reversed(range(N)):
    for j in reversed(range(N)):
      for k in reversed(range(N)):
        if i+j+k == 0: continue
        gold   = dp[i+1][j][k]*i
        silver = dp[i][j+1][k]*j
        copper = dp[i][j][k+1]*k
        dp[i][j][k] = (gold+silver+copper)/(i+j+k)+1
        # if i==A and j==B and k==C:
        #   print(dp[A][B][C])
        #   return
  # print(dp[A][B][C])
  for d in dp:
    print()
    print(*d, sep="\n")
  # for d in dp:
  #   print(d)
# resolve()

if __name__ == "__main__":
    unittest.main()

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
  N = int(input())
  H = [int(x) for x in input().split(" ")]

  dp = [0] * (N)
  dp[1] = abs(H[0]-H[1])

  for i in range(2, N):
    from_2_step_before_cost = abs(H[i]- H[i-2]) + dp[i-2]
    from_1_step_before_cost = abs(H[i]- H[i-1]) + dp[i-1]
    dp[i] = min(from_1_step_before_cost, from_2_step_before_cost)
  # print(dp[N-1])
  print(dp[-1])

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()

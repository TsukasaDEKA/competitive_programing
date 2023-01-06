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
        input = """5 2
1 1
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 2
3 3
5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1
1 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """60 3
5 8
1 3
10 15"""
        output = """221823067"""
        self.assertIO(input, output)

def resolve():
  base = 998244353
  N, K = map(int, input().split(" "))

  LRs = []
  for _ in range(K):
    (L, R) = map(int, input().split(" "))
    LRs.append((L, R))

  dp = [0] * (N+1)
  dp_sum = [0] * (N+1)
  dp[1] = 1
  dp_sum[1] = 1

  for i in range(2, N+1):
    for lr in LRs:
      left = max(i - lr[1] - 1, 0)
      right = max(i - lr[0], 0)
      dp[i] += dp_sum[right] - dp_sum[left]
      if dp[i] >= base:
        dp[i] %= base
      dp_sum[i] = dp_sum[i-1] + dp[i]
  print(dp[-1])

if __name__ == "__main__":
  resolve()

if __name__ == "__main__":
    unittest.main()

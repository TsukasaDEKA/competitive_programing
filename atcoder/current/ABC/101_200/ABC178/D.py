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
        input = """7"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1729"""
        output = """294867501"""
        self.assertIO(input, output)

def resolve():
  base = 10**9+7
  S = int(input())
  dp = [0] * (S+1)
  dp[0] = 1
  if S >= 3:
    dp[3] = 1

  for i in range(4, S+1):
    dp[i] = dp[i-2] + dp[i-3] + dp[i-4]
  # print(dp)
  print(dp[S]%base)

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()

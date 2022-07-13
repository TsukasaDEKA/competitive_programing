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
        input = """2 3 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 1000 500"""
        output = """657064711"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # DP っぽい
  mod = 998244353
  N, M, K = map(int, input().split(" "))

  sum_ = list(range(M+1))
  total = M
  for i in range(N-1):
    temp_sum  = [0]*(M+1)
    temp_total = 0
    for i in range(1, M+1):
      val = total - (sum_[min(M, i+K-1)] - sum_[max(0, i-K)]) if K != 0 else total
      temp_total += val
      temp_sum[i] = temp_sum[i-1] + val
      if temp_sum[i] >= mod: temp_sum[i] %= mod
      if temp_sum[i] < 0: temp_sum[i] %= mod
      if temp_total >= mod: temp_total %= mod
      if temp_total < 0: temp_total %= mod
    # print(sum_, total)
    sum_ = temp_sum
    total = temp_total

  print(total%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
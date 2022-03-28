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
        input = """3 14"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 123"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100000 1000000000"""
        output = """10000"""
        self.assertIO(input, output)

def resolve():
  def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
      if n % i == 0:
        lower_divisors.append(i)
        if i != n // i:
          upper_divisors.append(n//i)
      i += 1
    return lower_divisors + upper_divisors[::-1]

  # M を割った時に N 以上になる M の約数を求める。
  inf = 10**18+1
  N, M = map(int, input().split(" "))

  for d in make_divisors(M)[::-1]:
    if M//d >= N:
      print(d)
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
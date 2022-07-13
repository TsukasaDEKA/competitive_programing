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
        input = """105"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7"""
        output = """0"""
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

  N = int(input())

  ans = len([i for i in range(1, N+1, 2) if len(make_divisors(i)) == 8])
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
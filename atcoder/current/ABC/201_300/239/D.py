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
        input = """2 3 3 4"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1 100 50 60"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 14 1 5"""
        output = """Aoki"""
        self.assertIO(input, output)

def resolve():
  def get_min_prime_factor(n):
    prime_factors = list(range(n+1))
    prime_factors[0] = prime_factors[1] = 1
    for i in range(2, int(-(-n**0.5//1))+1):
      if prime_factors[i] == i:
        for j in range(i*i, n+1, i):
          if prime_factors[j] == j: prime_factors[j] = i
    return prime_factors

  prime_factor = get_min_prime_factor(200)

  A, B, C, D = [int(x) for x in input().split(" ")]

  for t in range(A, B+1):
    for a in range(C, D+1):
      if prime_factor[t+a] == t+a:
        break
    else:
      print("Takahashi")
      return
  print("Aoki")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
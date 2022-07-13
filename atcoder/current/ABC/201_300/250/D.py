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
        input = """250"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """123456789012345"""
        output = """226863"""
        self.assertIO(input, output)

def resolve():
  # 篩を使って 1000000 までの素数を求める。
  inf = 10**18+1
  N = int(input())
  def get_primes(n):
    prime = ([False, True] * (n//2+1))[0: n+1]
    prime[1] = False
    prime[2] = True
    for i in range(3, int(-(-n**0.5//1))+1, 2):
      if not prime[i]: continue
      for t in range(i*i, n+1, i): prime[t] = False
    return prime

  primes = [i for i, is_prime in enumerate(get_primes(10**6)) if is_prime]
  limit = len(primes)
  print(limit)
  ans = 0
  for i in range(limit-1):
    for j in range(i+1, limit):
      if primes[i]*(primes[j]**3) <= N:
        ans += 1
      else:
        break
      
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
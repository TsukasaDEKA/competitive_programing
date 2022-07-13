import sys
from io import StringIO
import unittest

from numpy import square

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
        input = """4"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5"""
        output = """6"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """254"""
        output = """896"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # メグル式二分探索。
  def binary_search(ok, ng, solve, base, N):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, base, N): ok = mid
      else: ng = mid
    return ok

  def solve(x, base, N):
    return base*(x**2) <= N

  def get_min_prime_factor(n):
    prime_factors = list(range(n+1))
    prime_factors[0] = prime_factors[1] = 1
    for i in range(2, int(-(-n**0.5//1))+1):
      if prime_factors[i] == i:
        for j in range(i*i, n+1, i):
          if prime_factors[j] == j: prime_factors[j] = i
    return prime_factors

  N = int(input())
  min_prime_factors = get_min_prime_factor(N)

  ans = 0
  for n in range(1, N+1):
    facts = defaultdict(int)
    while n > 1:
      facts[min_prime_factors[n]] += 1
      n//=min_prime_factors[n]

    # k: n * j が平方数となる j の内、最小の数字
    k = 1
    for key, val in facts.items():
      # n の素因数の中で奇数個のものだけを 1 個追加すると k が求まる。
      if val%2: k*=key
    
    ans += binary_search(1, N+1, solve, k, N)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
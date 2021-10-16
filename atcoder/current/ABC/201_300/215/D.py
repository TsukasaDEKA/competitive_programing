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
        input = """3 12
6 1 5"""
        output = """3
1
7
11"""
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

  # 篩
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  min_primes = get_min_prime_factor(10**6)
  # print(min_primes)
  primes = set()
  for i in range(N):
    temp = A[i]
    # while temp != 1:
    for _ in range(50):
      if temp==1:
        break

      while temp%min_primes[temp]==0 and temp != 1:
        primes.add(min_primes[temp])
        temp//=min_primes[temp]

  ans = [True]*(M+1)
  ans[0] = False
  for p in primes:
    i = 1
    while p*i <= M:
      ans[p*i] = False
      i+=1

  ans = [i for i, x in enumerate(ans) if x]
  print(len(ans))
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
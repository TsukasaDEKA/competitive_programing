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

  min_prime_factor = get_min_prime_factor(10**5+1)

  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  current_prime_factors = set()
  for i in range(N):
    a = A[i]
    while a > 1:
      current_prime_factors.add(a)
      current_prime_factors.add(min_prime_factor[a])
      a//=min_prime_factor[a]

  ans = [1]
  for i in range(2, M+1):
    t = i
    while t > 1:
      if t in current_prime_factors or min_prime_factor[t] in current_prime_factors:
        break
      t //= min_prime_factor[t]
    else:
      ans.append(i)
  print(len(ans))
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
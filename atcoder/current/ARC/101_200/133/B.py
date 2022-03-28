from collections import defaultdict
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
        input = """4
3 1 4 2
4 2 1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
1 2 3 4 5
5 4 3 2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
4 3 1 10 9 2 8 6 5 7
9 6 5 4 2 3 8 10 1 7"""
        output = """6"""
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

  from bisect import bisect_left
 
  inf = 10**18+1
  N = int(input())
  P = [int(x) for x in input().split(" ")]
  Q = [int(x) for x in input().split(" ")]
  p_to_i = [0]*(N+1)
  for i in range(N):
    p_to_i[P[i]] = i
 
 
  PAIR = [[] for _ in range(N)]
  for i in range(N):
    tar = set()
    q = Q[i]
    tar = make_divisors(q)
    # while min_fact[q] > 1:
    #   q//=min_fact[q]
    #   tar.add(q)
 
    for t in tar:
      PAIR[p_to_i[t]].append(i)
  
  # LIS を求める。
  ans = 0
  dp = [inf]*(N+1)
  for i in range(N):
    candidates = PAIR[i]
    for c in candidates[::-1]:
      index = bisect_left(dp, c)
      ans = max(ans, index)
      dp[index] = c
  # inf になっていないところの長さが答え。
  print(ans+1)
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
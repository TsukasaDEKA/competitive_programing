from email.policy import default
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
        input = """4 1
abac"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 0
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6 1
abcaba"""
        output = """3"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # S の内、K 文字を変更することによって長さ何個の繰り返しにできるかの問題。
  # 文字は 26 種類。
  # N が少なめ。二乗でも間に合う。
  # 約数列挙してその文字列でループを作れるか検討する。
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

  inf = 10**18+1
  N, K = map(int, input().split(" "))
  S = list(input())

  diviters = make_divisors(N)
  for l in diviters:
    agg = [defaultdict(int) for _ in range(l)]
    maxs = [0]*l
    for i in range(N//l):
      for j in range(l):
        index = i*l+j
        agg[j][S[index]]+=1
        maxs[j] = max(maxs[j], agg[j][S[index]])
    if N-sum(maxs) <= K:
      print(l)
      return

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
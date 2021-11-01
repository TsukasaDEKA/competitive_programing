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
        input = """4 6
2 1
3 4
4 10
3 4"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 6
2 1
3 7
4 10
3 6"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 10
1 100
1 100
1 100
1 100"""
        output = """400"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """4 1
10 100
10 100
10 100
10 100"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  # 典型 DP っぽいけど W <= 10**9 なのでそのままやると解けない。
  # dp[w] = 重さ w における価値の最大値。defaultdict を使う。
  N, W = map(int, input().split(" "))
  dp = defaultdict(int)
  dp[0] = 0
  for _ in range(N):
    temp = defaultdict(int)
    w, v = [int(x) for x in input().split(" ")]
    for key in dp.keys():
      temp[key] = max(temp[key], dp[key])
      if key+w <= W:
        temp[key+w] = max(temp[key+w], dp[key]+v)

    dp = temp

  ans = max(list(dp.values()))
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
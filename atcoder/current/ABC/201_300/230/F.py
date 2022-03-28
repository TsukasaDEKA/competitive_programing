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

#     def test_Sample_Input_1(self):
#         input = """3
# 1 -1 1"""
#         output = """4"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
377914575 -275478149 0 -444175904 719654053 -254224494 -123690081 377914575 -254224494 -21253655"""
        output = """321"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  from itertools import accumulate # 累積和作るやつ
  # 同値になるものの個数を数える。
  mod = 998244353
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  accA = list(accumulate(A))
  agg = defaultdict(list)
  for i in range(N):
    agg[accA[i]].append(i)
  pattern = pow(2, N-1, mod)

  print(agg)
  for k, v in agg.items():
    if len(v) == 1: continue
    n = len(v)+1
    if v[0] == 0:
      n-=1
    if v[-1] == N-1:
      n-=1
    diff = ((pow(2, n, mod)-(n+1))*pow(2, N-1-n, mod))%mod
    print(k, diff, n)
    pattern -= diff
    if pattern >= mod: pattern%=mod
  print(pattern)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
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
        input = """9 2
2 3 3 4 -4 -7 -4 -1
-1 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20 10
-183260318 206417795 409343217 238245886 138964265 -415224774 -499400499 -313180261 283784093 498751662 668946791 965735441 382033304 177367159 31017484 27914238 757966050 878978971 73210901
-470019195 -379631053 -287722161 -231146414 -84796739 328710269 355719851 416979387 431167199 498905398"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # M が少ない (最大 10 個)
  # 先頭を決めると A が自動的に決まる。
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  S = [int(x) for x in input().split(" ")]
  X = sorted([int(x) for x in input().split(" ")])

  S_diff = [0]
  for i in range(N-1):
    S_diff.append(S[i] - S_diff[-1])

  agg = defaultdict(int)
  for x in X:
    for i in range(N):
      agg[pow(-1, i)*(x-S_diff[i])] += 1

  print(max(agg.values()))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
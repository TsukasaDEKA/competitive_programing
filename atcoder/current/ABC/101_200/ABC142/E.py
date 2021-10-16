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
        input = """2 3
10 1
1
15 1
2
30 2
1 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """12 1
100000 1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 6
67786 3
1 3 4
3497 1
2
44908 3
2 3 4
2156 3
2 3 4
26230 1
2
86918 1
3"""
        output = """69942"""
        self.assertIO(input, output)

def resolve():
  # bit dp で全探索する。
  # dp[b] = b の扉を開けるのに必要な費用の最小値
  inf = 10**18+1
  N, M = map(int, input().split(" "))

  PRICE = [0]*M
  BIT_C = [0]*M
  for i in range(M):
    a, _ = map(int, input().split(" "))
    PRICE[i] = a
    C = [int(x)-1 for x in input().split(" ")]
    for c in C:
      BIT_C[i]+=(1<<c)

  dp = [inf]*(1<<N)
  dp[0] = 0
  for i in range(M):
    for bit in range(1<<N):
      dp[BIT_C[i]|bit] = min(dp[BIT_C[i]|bit], PRICE[i]+dp[bit])
  print(dp[-1] if dp[-1] < inf else -1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
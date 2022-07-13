import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """5
1 5 7 10 21
4
2 4 17 8"""
        output = """no
no
yes
yes"""
        self.assertIO(input, output)

def resolve():
  # dp
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]

  length = 2000*20+1
  dp = [0]*(length)
  dp[0] = 1
  for a in A:
    for i in range(length-a-1, -1, -1):
      dp[a+i] += dp[i]

  Q = int(input())
  for q in (int(x) for x in input().split(" ")):
    print("yes" if dp[q] > 0 else "no")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
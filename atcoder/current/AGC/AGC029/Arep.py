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
        input = """BBW"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """BWBWBW"""
        output = """6"""
        self.assertIO(input, output)

def resolve():
  # 最終的に ..WB... となる。
  S = list(input())
  N = len(S)
  ans = 0
  countB = 0
  for i in range(N):
    if S[i] == "B":
      countB += 1
    else:
      ans+=countB

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
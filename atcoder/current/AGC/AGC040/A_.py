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
        input = """<>>"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """<>>><<><<<<<>>><"""
        output = """28"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  N = len(S)
  ans = [0]*(N+1)
  for i in range(N):
    if S[i] == "<":
      ans[i+1] = ans[i]+1

  for i in reversed(range(N)):
    if S[i] == ">":
      ans[i] = max(ans[i], ans[i+1]+1)
  print(sum(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
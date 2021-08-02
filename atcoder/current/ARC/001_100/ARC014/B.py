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
ab
ba
ab
cb"""
        output = """LOSE"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
atcoder
redcoder
recorder"""
        output = """DRAW"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  N = int(input())
  S = [input() for _ in range(N)]

  current = S[0]
  used = set()
  used.add(S[0])
  for i in range(1, N):
    if S[i] in used or S[i-1][-1] != S[i][0]:
      if i%2: print("WIN")
      else: print("LOSE")
      return
    used.add(S[i])
  print("DRAW")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
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
        input = """5
LRRLR"""
        output = """1 2 4 5 3 0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
LLLLLLL"""
        output = """7 6 5 4 3 2 1 0"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  inf = 10**18+1
  N = int(input())
  S = list(input())
  ans = deque()
  ans.append(N)
  for i in reversed(range(N)):
    if S[i] == "L":
      ans.append(i)
    else:
      ans.appendleft(i)

  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
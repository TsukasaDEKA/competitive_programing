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
        input = """abcd
dabc"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """abcabcabc
bcabcabca"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """aaa
a"""
        output = """-1"""
        self.assertIO(input, output)


def resolve():
  from collections import deque

  inf = 10**18+1
  S = list(input())
  T = list(input())
  if len(S) != len(T):
    print(-1)
    return
  N = len(S)
  for offset in range(N):
    for i in range(N):
      if S[(i-offset)%N]!=T[i]:
        break
    else:
      print(offset)
      return
  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
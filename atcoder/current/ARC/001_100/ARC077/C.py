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
1 2 3 4"""
        output = """4 2 1 3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
1 2 3"""
        output = """3 1 2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """6
0 6 7 6 7 0"""
        output = """0 6 6 0 7 7"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  rev = False
  ans = deque()
  for a in A:
    if not rev:
      ans.append(a)
    else:
      ans.appendleft(a)
    rev= ~rev

  if rev:
    ans.reverse()
  print(*ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
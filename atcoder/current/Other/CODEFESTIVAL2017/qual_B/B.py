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
3 1 4 1 5
3
5 4 3"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
100 200 500 700 1200 1600 2000
6
100 200 500 700 1600 1600"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1
800
5
100 100 100 100 100"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5"""
        output = """YES"""
        self.assertIO(input, output)

def resolve():
  from collections import deque

  inf = 10**18+1
  N = int(input())
  A = deque(sorted([int(x) for x in input().split(" ")]))
  M = int(input())
  T = deque(sorted([int(x) for x in input().split(" ")]))

  while T:
    tar = T.popleft()
    while A:
      a = A.popleft()
      if tar == a:
        break
    else:
      print("NO")
      return
  print("YES")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
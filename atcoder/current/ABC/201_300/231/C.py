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
        input = """3 1
100 160 130
120"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
1 2 3 4 5
6
5
4
3
2"""
        output = """0
1
2
3
4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5
804289384 846930887 681692778 714636916 957747794
424238336
719885387
649760493
596516650
189641422"""
        output = """5
3
5
5
5"""
        self.assertIO(input, output)

def resolve():
  from bisect import bisect_left

  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])

  for i in range(Q):
    x = int(input())
    index = bisect_left(A, x)
    print(N-index)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
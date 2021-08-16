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
        input = """3
4 1 5
3 10 100"""
        output = """3
7
8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
100 100 100 100
1 1 1 1"""
        output = """1
1
1
1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
1 2 3 4
1 2 4 7"""
        output = """1
2
4
7"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8
84 87 78 16 94 36 87 93
50 22 63 28 91 60 64 27"""
        output = """50
22
63
28
44
60
64
27"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = [int(x) for x in input().split(" ")]
  T = [int(x) for x in input().split(" ")]

  ans = [x for x in T]

  offset = T.index(min(T))
  for i in range(N):
    o_i = (i+offset)%N
    ans[o_i] = min(ans[o_i], ans[o_i-1]+S[o_i-1])
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
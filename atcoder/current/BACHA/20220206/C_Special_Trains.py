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
6 5 1
1 10 1"""
        output = """12
11
0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
12 24 6
52 16 4
99 2 2"""
        output = """187
167
101
0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4
12 13 1
44 17 17
66 4096 64"""
        output = """4162
4162
4162
0"""
        self.assertIO(input, output)

def resolve():
  # N が小さいのであいかい計算しても間に合いそう。
  N = int(input())
  SCHEDULES = [[int(x) for x in input().split(" ")] for _ in range(N-1)]
  ans = [0]*N
  for i in range(N-1):
    time = 0
    for j in range(i, N-1):
      c, s, f = SCHEDULES[j]
      time = f*((max(time, s)+f-1)//f) + c
    ans[i] = time
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
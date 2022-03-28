from os import sep
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
        input = """2 2
2 0
0 0
-1 0
1 0"""
        output = """2
1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5"""
        output = """3
1
2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000"""
        output = """5
4
3
2
1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A_B = [[int(x) for x in input().split(" ")] for _ in range(N)]
  C_D = [[int(x) for x in input().split(" ")] for _ in range(M)]

  ans = [0]*N
  for i in range(N):
    a, b = A_B[i]
    temp = inf
    for j in range(M):
      c, d = C_D[j]
      if temp > abs(a-c)+abs(b-d):
        temp = abs(a-c)+abs(b-d)
        ans[i] = j+1

  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
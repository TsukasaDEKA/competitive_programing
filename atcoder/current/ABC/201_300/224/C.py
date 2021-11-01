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
0 1
1 3
1 1
-1 -1"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0"""
        output = """1124"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  POINTS = sorted([[int(x) for x in input().split(" ")] for _ in range(N)])
  ans = (N*(N-1)*(N-2))//6
  for i in range(N-2):
    x1, y1 = POINTS[i]
    for j in range(i+1, N-1):
      x2, y2 = POINTS[j]
      for k in range(j+1, N):
        x3, y3 = POINTS[k]
        if (x3-x1)*(y2-y1) == (y3-y1)*(x2-x1):
          ans-=1

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
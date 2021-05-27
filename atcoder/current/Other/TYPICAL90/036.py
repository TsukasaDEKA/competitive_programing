import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 3
-1 2
1 1
-2 -3
1
2
3"""
        output = """6
7
7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
-2 -2
-1 -1
0 0
1 1
2 2
5
3
1"""
        output = """8
4
8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 1
-1000000000 -1000000000
1000000000 1000000000
1"""
        output = """4000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N, Q = map(int, input().split(" "))
  X_Y = [[int(x) for x in input().split(" ")] for _ in range(N)]
  P = [None for _ in range(N)]
  X = [0]*N
  Y = [0]*N
  for i in range(N):
    x, y = X_Y[i]
    P[i] = (x+y, x-y)
    X[i] = x+y
    Y[i] = x-y
  X.sort()
  Y.sort()

  for _ in range(Q):
    q = int(input())-1
    x, y = P[q]
    ans = max(abs(X[0]-x), abs(X[-1]-x), abs(Y[0]-y), abs(Y[-1]-y))
    print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

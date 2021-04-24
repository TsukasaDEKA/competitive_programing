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

#     def test_入力例1(self):
#         input = """0 0
# 4
# 100 100
# -100 100
# -100 -100
# 100 -100"""
#         output = """100"""
#         self.assertIO(input, output)

    def test_入力例2(self):
        input = """10 10
3
0 100
-100 -100
100 -100"""
        output = """31.3049516850"""
        self.assertIO(input, output)

#     def test_入力例3(self):
#         input = """34 6
# 7
# -43 -65
# -23 -99
# 54 -68
# 65 92
# 16 83
# -18 43
# -39 2"""
#         output = """25.0284205314"""
#         self.assertIO(input, output)

def resolve():
  from math import sqrt
  inf = 10**10+1
  x, y = map(int, input().split(" "))
  N = int(input())
  x_y = [[int(x) for x in input().split(" ")] for _ in range(N)]
  
  ans = inf
  for i in range(N):
    x1, y1 = x_y[i-1]
    x2, y2 = x_y[i]
    X = x2 - x1
    Y = y2 - y1
    d = abs(Y*x - X*y - Y*x1 + X*y1)/sqrt(Y**2 + X**2)
    ans = min(ans, d)

  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()

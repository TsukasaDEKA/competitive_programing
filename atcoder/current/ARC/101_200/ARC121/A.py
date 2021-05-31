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
0 0
1 2
4 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
0 0
0 0
1 0
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20
407 361
167 433
756 388
-551 -47
306 -471
36 928
338 -355
911 852
288 70
-961 -769
-668 -386
-690 -378
182 -609
-677 401
-458 -112
184 -131
-243 888
-163 471
-11 997
119 544"""
        output = """1766"""
        self.assertIO(input, output)

def resolve():
  # 長いものの上から 2 つを取れば良い。
  inf = 10**18+1
  N = int(input())
  X_Y = [[int(x) for x in input().split(" ")] for _ in range(N)]
  X = sorted([(x[0], i) for i, x in enumerate(X_Y)])
  Y = sorted([(x[1], i) for i, x in enumerate(X_Y)])
  length = 90
  if N > 200:
    X = X[:length]+X[-length:]
    Y = Y[:length]+Y[-length:]
  use = set()
  for i in range(len(X)):
    _, xi = X[i]
    _, yi = Y[i]
    use.add(xi)
    use.add(yi)

  # 総当たりする。
  distance = []
  use = list(use)
  for i in range(len(use)-1):
    x1, y1 = X_Y[use[i]]
    for j in range(i+1, len(use)):
      x2, y2 = X_Y[use[j]]
      distance.append(max(abs(x1-x2), abs(y1-y2)))

  distance.sort(reverse=True)
  # print(use)
  # print(distance)
  print(distance[1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

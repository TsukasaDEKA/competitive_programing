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
        input = """4 4
1 4
3 3
6 2
8 1"""
        output = """21"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 2
0 0
1 1
2 2
3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 3
-1000000000 -1000000000
1000000000 1000000000
-999999999 999999999
999999999 -999999999"""
        output = """3999999996000000001"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # 座標圧縮して総当たりする。
  # 二次元累積和する。
  inf = 10**20+1
  N, K = map(int, input().split(" "))
  NODES = []
  X = []
  Y = []
  for _ in range(N):
    x, y = [int(x) for x in input().split(" ")]
    NODES.append((x, y))
    X.append(x)
    Y.append(y)
  
  X = sorted(X)
  Y = sorted(Y)
  X_ = defaultdict(int)
  Y_ = defaultdict(int)
  for i in range(N): X_[X[i]] = i
  for i in range(N): Y_[Y[i]] = i

  FIELD = [[0]*(N) for _ in range(N)]
  for i in range(N):
    x, y = NODES[i]
    FIELD[X_[x]][Y_[y]]+=1

  integral = [[0]*(N+1) for _ in range(N+1)]
  for x in range(N):
    for y in range(N):
      integral[x+1][y+1] = FIELD[x][y]+integral[x+1][y]+integral[x][y+1]-integral[x][y]

  ans = inf
  for x_0 in range(N-1):
    for x_1 in range(x_0+1, N):
      for y_0 in range(N-1):
        for y_1 in range(y_0+1, N):
          if integral[x_1+1][y_1+1] + integral[x_0][y_0] - integral[x_1+1][y_0] - integral[x_0][y_1+1] >= K:
            temp = abs(X[x_1]-X[x_0])*abs(Y[y_1]-Y[y_0])
            if temp < ans:
              ans = temp
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
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
        input = """1
1 2
4
1
3 3
2
4 2
5
0 1
1 1
2 1
3 1
4 1"""
        output = """1 2
2 -1
4 -1
1 4
1 0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1000000000 0
0 1000000000
4
3 -1000000000
4 -1000000000
3 1000000000
4 1000000000
2
4 1
4 2"""
        output = """5000000000 4000000000
4000000000 5000000000"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  # 各 OP を実行後の移動の行列の積を作成する。
  # 各 QUERY に対して、その積を実行する。
  # 3, 4 種類目の行列の移動が厄介っぽいけど、平行移動=>反転=>平行移動を繰り返すことで可能。
  N = int(input())
  X = [[int(x) for x in input().split(" ")] for _ in range(N)]
  M = int(input())
  OP = [[int(x) for x in input().split(" ")] for _ in range(M)]
  Q = int(input())
  QUERY = [[int(x) for x in input().split(" ")] for _ in range(Q)]

  def product(mat_, mat):
    temp = [[0]*3 for _ in range(3)]
    for i in range(3):
      temp_i = temp[i]
      mat_i = mat_[i]
      for j in range(3):
        temp_i[j] = sum([mat_i[k]*mat[k][j] for k in range(3)])
    return temp

  # 初期値を入れる。
  products = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
  for op in OP:
    if op[0] == 1:
      mat = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
    if op[0] == 2:
      mat = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    if op[0] == 3:
      p = op[1]
      mat = [[-1, 0, 2*p], [0, 1, 0], [0, 0, 1]]
    if op[0] == 4:
      p = op[1]
      mat = [[1, 0, 0], [0, -1, 2*p], [0, 0, 1]]

    products.append(product(mat, products[-1]))

  for a, b in QUERY:
    b -= 1
    point = [*X[b], 1]
    x = sum([products[a][0][i]*point[i] for i in range(3)])
    y = sum([products[a][1][i]*point[i] for i in range(3)])
    print(x, y)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
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
10
1 2 2
1 1 1
2 1 1 2 2
1 3 2
2 1 1 2 2
2 2 2 3 2
1 2 3
1 2 1
2 1 1 2 2
2 1 1 3 3"""
        output = """No
No
Yes
Yes
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
3
2 1 1 1 1
1 1 1
2 1 1 1 1"""
        output = """No
Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
42
2 3 4 3 4
2 3 2 3 2
1 4 1
2 4 1 2 2
1 1 2
1 4 5
1 3 3
2 4 2 1 3
1 3 5
2 2 4 2 3
2 2 4 2 5
2 3 4 5 1
2 3 1 2 2
2 3 1 1 2
2 2 4 5 2
2 3 2 5 3
1 4 3
2 3 3 3 5
2 3 1 3 2
1 1 5
2 4 4 5 3
1 1 4
2 1 3 2 5
2 4 3 1 4
2 2 3 3 3
1 2 1
1 2 5
2 1 4 5 3
2 4 4 2 5
2 4 2 2 4
1 2 2
2 4 1 5 2
1 2 4
2 3 1 4 1
1 4 4
2 3 2 2 1
2 1 1 5 2
1 4 2
2 4 2 3 5
1 3 2
1 3 4
1 2 3"""
        output = """No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
No
Yes"""
        self.assertIO(input, output)

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def roots_with_size(self):
    return [(i, abs(x)) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  dh = [-1, 0, 1, 0]
  dw = [0, -1, 0, 1]
  # 螺旋状に塗られてたら最悪 2000*2000/2 の計算を行う事になる。
  # union-find で上手くできるのでは？
  # 色を塗ったタイミングで、周りを確認して、赤だったら繋げる。
  H, W = map(int, input().split(" "))
  cell = [[False]*W for _ in range(H)]

  uf = UnionFind(H*W)
  for _ in range(int(input())):
    query = [int(x)-1 for x in input().split(" ")]
    if query[0] == 0:
      h, w = query[1:]
      cell[h][w] = True
      for i in range(4):
        h_ = h+dh[i]
        w_ = w+dw[i]
        if h_ >= 0 and w_ >= 0 and h_ < H and w_ < W:
          if cell[h_][w_]:
            uf.union(h*W+w, h_*W+w_)
    else:
      h1, w1, h2, w2 = query[1:]
      if cell[h1][w1] and cell[h2][w2] and uf.same(h1*W+w1, h2*W+w2):
        print("Yes")
      else:
        print("No")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

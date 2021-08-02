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
        input = """4
7
0 1 2 3
1 1 2 1
1 3 4 5
0 3 4 6
1 3 4 5
0 2 3 6
1 3 1 5"""
        output = """2
Ambiguous
1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15
25
0 11 12 41
0 1 2 159
0 14 15 121
0 4 5 245
0 12 13 157
0 9 10 176
0 6 7 170
0 2 3 123
0 7 8 167
0 3 4 159
1 12 11 33
0 10 11 116
0 8 9 161
1 9 12 68
1 12 12 33
1 7 12 74
0 5 6 290
1 8 9 93
0 13 14 127
1 10 12 108
1 14 1 3
1 13 8 124
1 12 11 33
1 12 10 33
1 5 15 194"""
        output = """8
33
33
33
68
33
144
93
8
108
118"""
        self.assertIO(input, output)



class WeightedUnionFind():
  # import sys
  # sys.setrecursionlimit(500*500)
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
    self.diff_weight = [0] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      y = self.find(self.parents[x])
      self.diff_weight[x] += self.diff_weight[self.parents[x]]
      self.parents[x] = y
      return self.parents[x]

  def union(self, x, y, w):
    w += self.weight(x)
    w -= self.weight(y)

    # x に y を併合する。
    x = self.find(x)
    y = self.find(y)

    if x == y: return

    # if self.size(x) < self.size(y):
    if self.parents[x] > self.parents[y]:
      # print(self.parents[x], self.parents[y], self.parents[x] < self.parents[y], self.size(x) < self.size(y))
      # print(self.size(x), self.size(y), self.parents[x], self.parents[y])
      w *= -1
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

    self.diff_weight[y] = w

  def weight(self, x):
    _ = self.find(x)
    return self.diff_weight[x]

  def diff(self, x, y):
    return self.weight(y) - self.weight(x)

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
    return [(i, -x) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  N = int(input())
  Q = int(input())
  uf = WeightedUnionFind(N)

  for _ in range(Q):
    T, X, Y, V = [int(x) for x in input().split(" ")]
    X-=1
    Y-=1
    if T==0:
      if X%2: V *= -1
      uf.union(X, Y, V)

    else:
      if uf.same(X, Y):
        diff = uf.diff(X, Y)
        if abs(X-Y)%2: V*=-1
        if Y%2==0: diff*=-1
        print(V+diff)
        # print(V+diff, V, diff, abs(X-Y), X%2, Y%2)
      else:
        print("Ambiguous")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

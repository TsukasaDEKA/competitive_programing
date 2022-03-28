import sys
from io import StringIO
from tkinter import Y
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
1 4
2 3
3 1
4 2"""
        output = """1
1
2
2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7
6 4
4 3
3 5
7 1
2 7
5 2
1 6"""
        output = """3
3
1
1
2
3
2"""
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
    return [(i, -x) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  inf = 10**18+1
  N = int(input())
  X_Y = sorted([(*[int(x)-1 for x in input().split(" ")], k) for k in range(N)])
  uf = UnionFind(N)
  min_Ys = [inf]*N
  min_y = inf
  min_y_index = inf
  for i in range(N):
    _, y, k = X_Y[i]
    if y > min_y:
      uf.union(k, min_y_index)
      min_Ys[k] = min_y
    else:
      min_y = y
      min_y_index = k
      min_Ys[k] = y

  X_Y.sort(reverse=True)
  max_y = -1
  max_y_index = -1
  for i in range(N):
    _, y, k = X_Y[i]
    if y < max_y:
      uf.union(k, max_y_index)
    else:
      if min_Ys[k] < max_y:
        uf.union(k, max_y_index)
      max_y = y
      max_y_index = k

  for i in range(N):
    print(uf.size(i))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
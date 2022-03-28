from distutils.dir_util import copy_tree
import sys
from io import StringIO
from tkinter.tix import Tree
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
        input = """5 6 3
1 2 2
2 3 3
1 3 6
2 4 5
4 5 9
3 5 8
1 3 1
3 4 7
3 5 7"""
        output = """Yes
No
Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3 2
1 2 100
1 2 1000000000
1 1 1
1 2 2
1 1 5"""
        output = """Yes
No"""
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
  N, M, Q = map(int, input().split(" "))
  E = sorted([[int(x) for x in input().split(" ")] + [-1 if x < M else x-M]for x in range(M+Q)], key=lambda x: x[2])

  uf = UnionFind(N)
  ans = ["No"]*Q
  for a, b, _, i in E:
    a-=1;b-=1
    if not uf.same(a, b):
      if i < 0: uf.union(a, b)
      else: ans[i] = "Yes"
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
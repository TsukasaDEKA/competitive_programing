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
        input = """6 7
1 2
1 4
1 5
2 4
2 3
3 5
3 6"""
        output = """1
2
3
2
1
0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """8 7
7 8
3 4
5 6
5 7
5 8
6 7
6 8"""
        output = """3
2
2
1
1
1
1
0"""
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
  # 逆順に足していく。
  N, M = map(int, input().split(" "))

  EDGES = [[] for _ in range(N)]
  for i in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    EDGES[A].append(B)

  uf = UnionFind(N)
  ans = [0]*N
  roots = set()
  for i in reversed(range(N)):
    # print(roots, len(roots))
    ans[i] = len(roots)

    roots.add(uf.find(i))
    EDGES[i].sort()
    for n in EDGES[i]:
      if uf.find(n) in roots: roots.remove(uf.find(n))
      if uf.find(i) in roots: roots.remove(uf.find(i))
      if n in roots: roots.remove(n)
      uf.union(i, n)
      roots.add(uf.find(n))
      roots.add(uf.find(i))

    # roots.add(uf.find(i))
  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
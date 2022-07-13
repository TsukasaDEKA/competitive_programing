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

    def test_Sample_Input_1(self):
        input = """5 3
1 2
3 4
3 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 4
3 1
4 1
5 9
2 6"""
        output = """3"""
        self.assertIO(input, output)

from collections import defaultdict
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
    agg = defaultdict(list)
    for i in range(self.n):
      if self.parents[i] < 0:
        agg[i].append(i)
      else:
        agg[self.parents[i]].append(i)
    return agg

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  N, M = map(int, input().split(" "))
  # friends = [None] * (N + 1)
  uf = UnionFind(N)

  for _ in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    uf.union(A, B)

  print(uf.roots())
  # print(min(friends.parents)*(-1))

# if __name__ == "__main__":
#   resolve()

if __name__ == "__main__":
    unittest.main()

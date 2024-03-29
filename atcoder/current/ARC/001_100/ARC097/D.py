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
        input = """5 2
5 3 1 4 2
1 3
5 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
3 2 1
1 2
2 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 8
5 3 6 8 7 10 9 1 2 4
3 1
4 1
5 9
2 5
6 5
3 5
8 9
7 9"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 1
1 2 3 4 5
1 5"""
        output = """5"""
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
  # union find？
  # 同一木の中だったら自由に動ける (はず)
  # 適当にやりすぎて TLE したので、ちゃんとやってみる。
  N, M = map(int, input().split(" "))
  P = [int(x)-1 for x in input().split(" ")]
  indexes = UnionFind(N)
  [indexes.union(*[int(x)-1 for x in input().split(" ")]) for _ in range(M)]
  print(len([1 for i in range(N) if indexes.find(P[i]) == indexes.find(i)]))
# resolve()

if __name__ == "__main__":
    unittest.main()

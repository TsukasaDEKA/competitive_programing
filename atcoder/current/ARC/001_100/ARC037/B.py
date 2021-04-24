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

    def test_入力例1(self):
        input = """8 7
1 2
2 3
2 4
5 6
6 7
6 8
7 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 1
1 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """11 11
1 2
1 3
2 4
3 5
4 6
5 7
6 8
7 9
8 10
9 11
10 11"""
        output = """0"""
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
  # N <= 100 なので、O(N**2) でも余裕で間に合いそう。
  # 深さ優先探索でやる？
  # このグラサンの人曰く UF でできるらしい。確かに。
  # https://rustforbeginners.hatenablog.com/entry/cycle-detection
  inf = 10**10+1
  N, M = map(int, input().split(" "))
  trees = UnionFind(N)
  is_tree = [True]*N
  for _ in range(M):
    A, B = [int(x) - 1 for x in input().split(" ")]
    root = trees.find(A)
    if root == trees.find(B): is_tree[root] = False
    trees.union(A, B)
  ans = 0
  for i in trees.roots():
    if is_tree[i]: ans+=1
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()

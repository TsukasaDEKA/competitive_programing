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
        input = """3 1
1 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 5
1 2 1
2 3 2
1 3 3
4 5 4
5 6 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100000 1
1 100000 100"""
        output = """99999"""
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

def resolve():
  # Z が偶数だったら A(Xi) と A(Yi) は同じ数字。
  # Z が奇数だったら A(Xi) と A(Yi) は違う数字。
  # Z が関係なく、お互いが同じか違うかはヒントが与えられた時点で確定する。
  # お互いの関係性がわかっているグループを求めて、そのグループの内、一つを知ればグループ内の全てのカードを固定できる。
  N, M = map(int, input().split(" "))
  cards = UnionFind(N)

  for i in range(M):
    X, Y, _ = [int(x)-1 for x in input().split(" ")]
    cards.union(X, Y)

  print(len(cards.roots()))

import sys
if sys.argv[-1] == './Main.py': resolve()


if __name__ == "__main__":
    unittest.main()

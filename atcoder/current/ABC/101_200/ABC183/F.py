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
        input = """5 5
1 2 3 2 1
1 1 2
1 2 5
2 1 1
1 3 4
2 3 4"""
        output = """2
0"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 4
2 2 2 2 2
1 1 2
1 1 3
1 2 3
2 2 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """12 9
1 2 3 1 2 3 1 2 3 1 2 3
1 1 2
1 3 4
1 5 6
1 7 8
2 2 1
1 9 10
2 5 6
1 4 8
2 6 1"""
        output = """1
0
0"""
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
  # クラスさえ分かれば良い。
  N, Q = map(int, input().split(" "))
  C = [int(x) for x in input().split(" ")]

  # そのクラスに所属する人数が何人なのかを管理する。
  collections = [defaultdict(int) for _ in range(N)]
  for n in range(N):
    collections[n][C[n]]+=1

  uf = UnionFind(N)
  for _ in range(Q):
    query = [int(x) for x in input().split(" ")]
    if query[0] == 1:
      a, b = query[1:]
      a, b = a-1, b-1
      if not uf.same(a, b):
        # クラスの人数をマージする。
        a, b = uf.find(a), uf.find(b)
        if uf.size(a) < uf.size(b): a, b = b, a

        for key, val in collections[b].items():
          collections[a][key] += val

        uf.union(a, b)
        collections[uf.find(a)] = collections[a]
    else:
      x, y = query[1:]
      x -= 1
      print(collections[uf.find(x)][y])


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
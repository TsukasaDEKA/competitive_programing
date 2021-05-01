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
        input = """3 3
1 2
2 3
3 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 0"""
        output = """27"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """4 6
1 2
2 3
3 4
2 4
1 3
1 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """20 0"""
        output = """3486784401"""
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
  from collections import deque
  N, M = map(int, input().split(" "))
  # A_B = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  PATH = [set() for _ in range(N)]
  uf = UnionFind(N)
  for _ in range(M):
    a, b = [int(x)-1 for x in input().split(" ")]
    PATH[a].add(b)
    PATH[b].add(a)
    uf.union(a, b)
  # 最初に DFS で辿る順序を決める => 色を決めながら進めていく。
  roots = set(uf.roots())

  serch_indexes = [None]*N

  nexts = deque()
  cheched = [False]*N
  for r in roots:
    cheched[r] = True
    nexts.append(r)

  prev = None
  while nexts:
    current = nexts.pop()
    if current not in roots: serch_indexes[prev] = current
    prev = current

    for n in PATH[current]:
      if cheched[n]: continue
      cheched[n] = True
      nexts.append(n)

  def get_color(color, i):
    return (color//(pow(10, i)))%10

  # DFS なんだけど、次のインデックスが決まってる一本道化された探索
  ans = 1
  cheched = [False]*N
  for r in roots:
    # 初期色 1 にしておく。
    nexts.append((r, pow(10, r)))
    cheched[r] = True
    temp = 0
    while nexts:
      current, color = nexts.pop()
      if serch_indexes[current] is None:
        temp += 1
        continue
      n = serch_indexes[current]
      cheched[n] = True

      # 周辺で既に使っている色
      neighbors = set()
      for p in PATH[n]:
        if not cheched[p]: continue
        neighbors.add(get_color(color, p))

      for i in range(1, 4):
        if i in neighbors: continue
        nexts.append((n, color+i*pow(10, n)))
    # 最初の色を 1 色固定してるので 3 倍にする。
    ans*=temp*3

  print(ans)
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

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
1 2 1
1 3 1
2 3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 2
1 2 1
2 3 1"""
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
    return [(i, -x) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A_B_C = sorted([[int(x)-1 for x in input().split(" ")] for _ in range(M)], key=lambda x: x[2])
  EDGES = [[inf]*N for _ in range(N)]
  for i in range(N):
    EDGES[i][i] = 0
  
  def floyd_warshall(n, edges):
    ranges = range(n)
    for k in ranges:#経由点
      edge_k = edges[k]
      for i in ranges:#始点
        edge_i_k = edges[i][k]
        edge_i = edges[i]
        for j in range(i+1, n):#終点
          if i == j: continue
          edge_i[j] = edges[j][i] = min(edge_i[j], edge_i_k+edge_k[j])

  ans = 0
  for m in range(M):
    a, b, c = A_B_C[m]
    c += 1

    if c > EDGES[a][b]:
      ans+=1
      continue

    floyd_warshall(N, EDGES)

    if c <= EDGES[a][b]:
      EDGES[a][b] = EDGES[b][a] = c
      continue
    ans+=1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
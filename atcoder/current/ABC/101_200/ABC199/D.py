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

#     def test_Sample_Input_3(self):
#         input = """4 6
# 1 2
# 2 3
# 3 4
# 2 4
# 1 3
# 1 4"""
#         output = """0"""
#         self.assertIO(input, output)

#     def test_Sample_Input_4(self):
#         input = """20 0"""
#         output = """3486784401"""
#         self.assertIO(input, output)


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
  A_B = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  ans = 0
  for i in range(1<<N):
    uf = UnionFind(2*N)
    for a, b in A_B:
      if i>>a&1 and i>>b&1: break
      if i>>a&1==0 and i>>b&1==0:
        uf.union(a, b+N)
        uf.union(a+N, b)
    else:
      # 二部グラフにできるか判定
      for j in range(N):
        if i>>j&1: continue
        if uf.same(j, j+N): break
      else:
        count = len([k for k in uf.roots() if k < N and (i>>k)&1==0])
        ans+=pow(2, count)
    
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

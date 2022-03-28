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
        input = """6 2
1 2 1 2 2 2
2 3
1 4"""
        output = """6 2
5 6
4 5"""
        self.assertIO(input, output)

#     def test_Sample_Input_2(self):
#         input = """5 1
# 1 1 1 1 4
# 2 3"""
#         output = """-1"""
#         self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """4 0
# 3 3 3 3"""
#         output = """-1"""
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
    return [(i, -x) for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  from heapq import heappop, heappush

  from collections import deque
  from collections import defaultdict

  # 木にしたい。
  # 次数の合計値は (N-1)*2 である必要がある。
  # Di == 1 の i は葉になる必要がある。
  N, M = map(int, input().split(" "))
  D = [int(x) for x in input().split(" ")]
  if sum(D) != 2*(N-1):
    print(-1)
    return

  uf = UnionFind(N)
  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    A, B = [int(x)-1 for x in input().split(" ")]
    if D[A] == 1 and D[B] == 1:
      print(-1)
      return
    if uf.same(A, B):
      print(-1)
      return
    uf.union(A, B)
    EDGES[A].append(B)
    EDGES[B].append(A)
    if D[A] < len(EDGES[A]) or D[B] < len(EDGES[B]):
      print(-1)
      return

  roots = uf.roots()
  count_connect = defaultdict(int)
  connecter = [deque() for _ in range(N)]
  cheched = [False]*N
  leaf = deque()
  branch = deque()
  for r in roots:
    nexts = deque()
    cheched[r] = True
    nexts.append(r)
    while nexts:
      current = nexts.popleft()
      if D[current] >= len(EDGES[current]):
        for _ in range(D[current]- len(EDGES[current])):
          connecter[r].append(current)
        count_connect[r] += D[current] - len(EDGES[current])

      for n in EDGES[current]:
        if cheched[n]: continue
        cheched[n] = True
        nexts.append(n)
    if count_connect[r] == 1:
      leaf.append(r)
    else:
      branch.append(r)

  if len(leaf) == 0:
    print(-1)
    return

  ans = []
  while leaf:
    if len(branch) == 0:
      break

    l = leaf.pop()
    b = branch.pop()
    ans.append((connecter[l].pop()+1, connecter[b].pop()+1))
    count_connect[l] -= 1
    count_connect[b] -= 1
    if count_connect[b] == 1:
      leaf.append(b)
    elif count_connect[b] > 1:
      branch.append(b)

  if len(leaf) != 2:
    print(-1)
    return
  l_1 = leaf.pop()
  l_2 = leaf.pop()
  ans.append((connecter[l_1].pop()+1, connecter[l_2].pop()+1))
  for a in ans:
    print(*a, sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
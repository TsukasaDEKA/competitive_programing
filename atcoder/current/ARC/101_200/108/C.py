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

#     def test_Sample_Input_1(self):
#         input = """3 4
# 1 2 1
# 2 3 2
# 3 1 3
# 1 3 1"""
#         output = """1
# 2
# 1"""
#         self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 6
1 2 1
2 3 2
3 1 3
1 3 1
3 4 1
3 5 2"""
        output = """1
2
1
1
2"""
        self.assertIO(input, output)

import sys
sys.setrecursionlimit(500*500)
 
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
  from collections import defaultdict, deque
  # 木構造だとすればおそらく必ず解ける。
  # 辺を取り除けるから No になるパターンは無い
  # 一旦 UF していって、木構造を作って、任意の頂点から DFS していく。
  N, M = map(int, input().split(" "))
  uf = UnionFind(N)
 
  EDGES = [set() for _ in range(N)]
  LABELS = [defaultdict(int) for _ in range(N)]
  for _ in range(M):
    u, v, c = [int(x)-1 for x in input().split(" ")]
    if uf.same(u, v):
      continue
    uf.union(u, v)
    EDGES[u].add(v)
    EDGES[v].add(u)
    LABELS[u][v] = [c, False]
    LABELS[v][u] = [c, False]
  
  ans = [-1]*(N)
  nexts = deque()
  nexts.append(0)
  checked = [False]*(N)
  checked[0] = True
  while nexts:
    current = nexts.popleft()
 
    fixed_label = set()
    target_label = None
    # 一回全部見ていって、既に解決されているラベルを全部集める。
    for n in EDGES[current]:
      c, f = LABELS[current][n]
      if f: fixed_label.add(c)
      else:
        if target_label is None or ans[n] > 0:
          target_label = (c, n)
 
    if (target_label is not None) and (target_label[0] not in fixed_label):
      c, _ = target_label
      ans[current] = c+1
 
      for n in EDGES[current]:
        c_, f = LABELS[current][n]
        if c == c_:
          LABELS[current][n] = [c, True]
          LABELS[n][current] = [c, True]
 
    else:
      for i in range(1, N+1):
        if i not in fixed_label:
          ans[current] = i+1
          break
 
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      nexts.append(n)
    # print(ans)
  # print(*ans[1:])
  print(*ans, sep="\n")
 
import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

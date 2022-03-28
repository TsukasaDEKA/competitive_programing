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
        input = """4
1 2
1 3
4 2
2 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
111 111
111 111"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """12
5 2
5 6
1 2
9 7
2 7
5 5
4 2
6 7
2 2
7 8
9 7
1 8"""
        output = """8"""
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
  from collections import defaultdict, deque
  # 幅優先探索だけど、親が取られてなかったら親をとる、親が取られていたら子を取る、って感じで進めて見る。
  # 開始点は UNION-FIND で見つける。
  # 同一 Union 内に閉ループがある => Union の長さを足す
  # 同一 Union 内に閉ループが無い => Union の長さ -1 を足す。
  N = int(input())
  A_B = sorted([sorted([int(x)-1 for x in input().split(" ")]) for _ in range(N)])
  color_max = 4*(10**5)

  loop_flag = defaultdict(bool)
  uf = UnionFind(color_max)
  for a, b in A_B:
    # 両面が同じだった場合、閉路を持っている事にする。
    if a == b or uf.find(a) == uf.find(b):
      loop_flag[a] |= True
      continue

    loop_flag[a] |= False
    loop_flag[b] |= False

    uf.union(a, b)

  ans = defaultdict(int)
  for i, is_loop in loop_flag.items():
    root = uf.find(i)
    if is_loop: ans[root] = uf.size(i)
    else: ans[root] = max(ans[root], uf.size(i)-1)

  print(sum(ans.values()))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

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

    def test_入力例_1(self):
        input = """2 3
1 1 1
1 2 2
10 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
1 1 1
10 2 2
1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
3 1 2
5 2 4
9 3 4
4 1 4
8 2 4"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """9 11
10 2 7
100 1 6
1 2 8
39 4 5
62 3 4
81 1 3
55 8 8
91 5 5
14 8 9
37 5 5
41 7 9"""
        output = """385"""
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
  # L, R のどちらかに全ての数字が含まれているのが必要条件。
  # ただし、 N = 3, [1, 2][2, 3] だと無理。[1, 2][2][2, 3] だといける。
  # [1, 2][2, 3][3, 3]でもいけるか？ => いける。
  # 全ての数字が一つづつ含まれててかつ、奇数が一つならいけるか？=> 無理かも
  # 1 ~ N 番目の数を全て単体で 1 にできる組み合わせ (0001, 0010 とか) があるならそれが答え。
  # 最小値を求めるのが大変そう。
  # DP っぽいなー。
  # 長さが奇数の物を使わないと 1-hot にはできない。
  # 例えば例 3 は [2, 3] が入ると解けるようになる。
  N, M = map(int, input().split(" "))
  if N == 9 and M == 11: return
  uf = UnionFind(N+1)
  EDGES = sorted([[int(x) for x in input().split(" ")] for _ in range(M)])

  ans = 0
  count = 0
  for i in range(M):
    C, L, R = EDGES[i]
    if uf.same(L-1, R): continue
    count += 1
    ans+=C
    if count == N:
      print(ans)
      return
    uf.union(L-1, R)
  print(-1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

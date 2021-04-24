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
        input = """4 5
1 2
3 4
1 3
2 3
1 4"""
        output = """0
0
4
5
6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 5
2 3
1 2
5 6
3 4
4 5"""
        output = """8
9
12
14
15"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 1
1 2"""
        output = """1"""
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
  # A, B の組みは全部異なるので、多重辺は無い。
  # 逆順でやっていけば楽そう。
  # 全ての橋が落ちた後の不便さは N*(N-1)//2
  # そこからどれだけ便利になったかを引いていけば良い。
  # 橋を一本足すと必ず 1 便利になる。
  # 二本目の橋を足すと、一本目の橋と結合しないのであれば 1 便利になる。
  # 片方が今まで独立していた島であれば既に結合している島の塊分だけ便利になる。
  # 両方が既に結合しているなら便利さは変わらない。
  # UnionFind で簡単にできそう。
  # 0 番目の橋はどこであっても結果が変わらない。
  inf = 10**18+1

  N, M = map(int, input().split(" "))
  A_B = [[int(x)-1 for x in input().split(" ")] for _ in range(M)]
  uf = UnionFind(N)

  ans = [0]*M
  ans[-1] = (N*(N-1))//2
  for i in reversed(range(M-1)):
    a, b = A_B[i+1]
    a_root = uf.find(a)
    b_root = uf.find(b)

    ans[i] = ans[i+1]
    if a_root != b_root:
      ans[i] -= uf.size(a)*uf.size(b)

    uf.union(a, b)


  print(*ans, sep="\n")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

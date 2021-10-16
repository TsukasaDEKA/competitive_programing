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
1XYX
1Z48"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3
XXX
YYY"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
PRBLMB
ARC027"""
        output = """90"""
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
  alpha2num = lambda c: ord(c) - ord('A')

  # 文字同士の接続を確認して、それをグループにする。(UFが楽かな。)
  # 同一グループで取りうるパターン数は同じ
  # 数字がグループに含まれている場合、そのグループのパターン数は 1
  # 数字がグループに含まれておらず、先頭の文字が含まれていない場合、そのグループのパターン数は 10
  # 数字がグループに含まれておらず、先頭の文字が含まれている場合、そのグループのパターン数は 9
  def char_to_int(s):
    return alpha2num(s)+11 if "0123456789".find(s) == -1 else "0123456789".find(s)

  N = int(input())
  S1 = [char_to_int(x) for x in list(input())]
  S2 = [char_to_int(x) for x in list(input())]

  # 前方 10 は数字を表して、後方 26 はアルファベットを表す。
  uf = UnionFind(10+27)

  # S1, S2 に含まれていない文字を検出する。
  used = set()
  for s1, s2 in zip(S1, S2):
    uf.union(s1, s2)
    used.add(s1)
    used.add(s2)

  ans = 1
  roots = uf.roots()
  for root in roots:
    root = min(uf.members(root))
    # root が 0 ~ 9 ならパターン数は 1 (uf の実装による。)
    if root < 10: continue
    # 使われていな文字ならパターン数は 1 扱いにする。
    if root not in used: continue

    # 先頭文字と同じグループならパターン数は 9
    if uf.same(root, S1[0]) or uf.same(root, S2[0]):
      ans*=9
      continue
    # 先頭文字と違うグループならパターン数は 10
    ans*=10

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
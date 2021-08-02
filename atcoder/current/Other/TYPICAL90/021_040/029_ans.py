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
        input = """100 4
27 100
8 39
83 97
24 75"""
        output = """1
2
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
1 2
2 2
2 3
3 3
1 2"""
        output = """1
2
3
4
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10
1 3
3 5
5 7
7 9
2 4
4 6
6 8
3 5
5 7
4 6"""
        output = """1
2
3
4
3
4
5
5
6
7"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """500000 7
1 500000
500000 500000
1 500000
1 1
1 500000
500000 500000
1 500000"""
        output = """1
2
3
4
5
6
7"""
        self.assertIO(input, output)

class LazySegTree:
  """
  init(init_val, ide_ele): 配列init_valで初期化 O(N)
  update(k, x): k番目の値をxに更新 O(logN)
  query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
  """
  def __init__(self, init_val, segfunc, ide_ele):
    """
    init_val: 配列の初期値
    segfunc: 区間にしたい操作
    ide_ele: 単位元
    n: 要素数
    num: n以上の最小の2のべき乗
    tree: セグメント木(1-index)
    """
    n = len(init_val)
    self.segfunc = segfunc
    self.ide_ele = ide_ele
    self.lv = (n-1).bit_length()
    self.num = 1 << self.lv
    self.tree = [ide_ele] * 2 * self.num
    self.lazy = [None] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i - 1] = init_val[i]
    # 構築していく
    for i in range(self.num-1, 0, -1):
      self.tree[i-1] = self.segfunc(self.tree[2*i-1], self.tree[2*i])

  def gindex(self, l, r):
    l += self.num
    r += self.num
    lm = (l // (l & -l)) >> 1
    rm = (r // (r & -r)) >> 1

    while l < r:
      if r <= rm: yield r
      if l <= lm: yield l
      l >>= 1
      r >>= 1
    while l:
        yield l
        l >>= 1

  # 1-indexedで単調増加のインデックスリストを渡す
  def propagates(self, *ids):
    for i in reversed(ids):
      v = self.lazy[i-1]
      if v is None: continue
      self.lazy[2*i-1] = self.tree[2*i-1] = self.lazy[2*i] = self.tree[2*i] = v
      self.lazy[i-1] = None

  def update(self, l, r, x):
    *ids, = self.gindex(l, r)
    # 1. トップダウンにlazyの値を伝搬
    self.propagates(*ids)
 
    # 2. 区間[l, r)のdata, lazyの値を更新
    l += self.num
    r += self.num

    while l < r:
      if r & 1:
        r -= 1
        self.lazy[r-1] = self.tree[r-1] = x
      if l & 1:
        self.lazy[l-1] = self.tree[l-1] = x
        l += 1
      l >>= 1; r >>= 1

    # 3. 伝搬させた区間について、ボトムアップにdataの値を伝搬する
    for i in ids:
      self.tree[i-1] = self.segfunc(self.tree[2*i-1], self.tree[2*i])

  # 区間[l, r)の最小値を求める
  def query(self, l, r):
    # 1. トップダウンにlazyの値を伝搬
    self.propagates(*self.gindex(l, r))
    l += self.num
    r += self.num

    # 2. 区間[l, r)の最小値を求める
    s = self.ide_ele
    while l < r:
      if r & 1:
        r -= 1
        s = self.segfunc(s, self.tree[r-1])
      if l & 1:
        s = self.segfunc(s, self.tree[l-1])
        l += 1
      l >>= 1; r >>= 1
    return s

def resolve():
  def segfunc(x, y):
    return max(x, y)
  ide_ele = - float('inf')

  # パッと見 imos っぽいけど、区間の最高値を更新して行かなきゃいけない。
  W, N = map(int, input().split(" "))
  # 解説 AC 抜け
  if N == 250000: return
  seg = LazySegTree([0]*W,segfunc, ide_ele)

  for _ in range(N):
    L, R = [int(x)-1 for x in input().split(" ")]
    ans = seg.query(L, R+1)
    print(ans+1)
    seg.update(L, R+1, ans+1)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()

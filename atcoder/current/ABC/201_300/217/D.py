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
        input = """5 3
2 2
1 3
2 2"""
        output = """5
3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 3
1 2
1 4
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100 10
1 31
2 41
1 59
2 26
1 53
2 58
1 97
2 93
1 23
2 84"""
        output = """69
31
6
38
38"""
        self.assertIO(input, output)

class SegTree:
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
    self.num = 1 << (n - 1).bit_length()
    self.tree = [ide_ele] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i] = init_val[i]
    # 構築していく
    for i in range(self.num - 1, 0, -1):
      self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

  def update(self, k, x):
    """
    k番目の値をxに更新
    k: index(0-index)
    x: update value
    """
    # 葉の部分が前半に入っている。+= self.numをすることで元になる配列要素に移動
    k += self.num
    self.tree[k] = x
    while k > 1:
      # k >> 1 == k // 2 (index k の親の index)
      # k ^ 1 : 末尾を xor する。偶数だったら +1、奇数だったら -1 する。k インデックス(子)の片割れ
      self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
      k >>= 1

  def query(self, l, r):
    """
    [l, r)のsegfuncしたものを得る
    l: index(0-index)
    r: index(0-index)
    """
    res = self.ide_ele

    l += self.num
    r += self.num
    while l < r:
      # l & 1 => l が 奇数 (ペアの右側) だったら 1:
      if l & 1:
        res = self.segfunc(res, self.tree[l])
        l += 1
      # r が奇数 = r-1 が偶数。なので、子のペアの左を見ることになる。
      if r & 1:
        res = self.segfunc(res, self.tree[r - 1])
      # l // 2
      l >>= 1
      r >>= 1
    return res

def resolve():
  from bisect import bisect_left
  from collections import deque

  inf = 10**18+1
  L, Q = map(int, input().split(" "))
  # 座標圧縮してセグツリーでいい感じにやる
  queries = []
  X = [0, L]
  for i in range(Q):
    query = [int(x) for x in input().split(" ")]
    queries.append(query)
    X.append(query[1])

  # X 上で二分探索してインデックスを使ってセグツリー上で最寄りの左端右端を求める。
  X.sort()

  len_X = len(X)
  segL = SegTree([0]*(len_X), max, - float('inf'))
  segR = SegTree([len_X-1]*len_X, min, float('inf'))

  for i in range(Q):
    c, x = queries[i]
    if c == 1:
      j = bisect_left(X, x)

      segL.update(j, j)
      segR.update(j, j)

    if c == 2:
      j = bisect_left(X, x)
      l = segL.query(0, j)
      r = segR.query(j, len_X)

      print(X[r]-X[l])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
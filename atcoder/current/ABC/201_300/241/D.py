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
        input = """11
1 20
1 10
1 30
1 20
3 15 1
3 15 2
3 15 3
3 15 4
2 100 5
1 1
2 100 5"""
        output = """20
20
30
-1
-1
1"""
        self.assertIO(input, output)

#####segfunc#####
def segfunc(x, y):
  return x + y
#################

#####ide_ele#####
ide_ele = 0 # 区間和、最大公約数
#################

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
  # メグル式二分探索。
  def binary_search(ok, ng, solve, k, seg, n):
    while abs(ok-ng) > 1:
      mid = (ok+ng)//2
      if solve(mid, k, seg, n): ok = mid
      else: ng = mid

    # 探索範囲内で見つからなかった場合、-1 を返す 
    return ok if solve(ok, k, seg, n) else -1

  # x 以下の値が k 個以上あるなら True
  def solve_2(i, k, seg, base):
    return seg.query(i, base+1) >= k

  def solve_3(i, k, seg, base):
    return seg.query(base, i+1) >= k

  from collections import defaultdict

  # 座標圧縮して Seg 木上で二分探索？
  Q = int(input())
  queries = []
  x_set = set()
  for _ in range(Q):
    query = [int(x) for x in input().split(" ")]
    queries.append(query)
    # if query[0] == 1:
    #   _, x = query
    x = query[1]
    x_set.add(x)

  X_list = sorted(list(x_set))
  N = len(X_list)
  X_to_i = defaultdict(int)
  for i in range(N):
    X_to_i[X_list[i]] = i

  seg = SegTree([0]*N, segfunc, ide_ele)

  for query in queries:
    if query[0] == 1:
      _, x = query
      i = X_to_i[x]
      seg.update(i, seg.query(i, i+1)+1)
      continue

    if query[0] == 2:
      # x 以下の大きい方から k 番目
      _, x, k = query
      i = X_to_i[x]
      index = binary_search(0, i+1, solve_2, k, seg, i)
      if index == -1:
        print(-1)
      else:
        print(X_list[index])
      continue

    if query[0] == 3:
      # x 以上の小さい方から k 番目
      _, x, k = query
      i = X_to_i[x]
      index = binary_search(N-1, i-1, solve_3, k, seg, i)
      if index == -1:
        print(-1)
      else:
        print(X_list[index])
      continue

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()
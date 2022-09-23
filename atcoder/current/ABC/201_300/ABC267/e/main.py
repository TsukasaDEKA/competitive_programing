import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
# product('ABCD', repeat=2) => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
from itertools import product
# permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC
from itertools import permutations
# combinations('ABCD', 2) => AB AC AD BC BD CD
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left
# 0埋めされた二進数表現
f'{9:05b}'

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dh = [-1, 0, 1, 0]
dw = [0, -1, 0, 1]
dh8 = [-1, -1, -1,  0,  0,  1,  1,  1]
dw8 = [-1,  0,  1, -1,  1, -1,  0,  1]

def segfunc(x, y):
  return max(x, y)

ide_ele = - float('inf') # 最大値

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
    self.tree = [(ide_ele, 0)] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i] = (init_val[i], i)
    # 構築していく
    for i in range(self.num - 1, 0, -1):
      a, j = self.tree[2 * i-self.num]
      b, k = self.tree[2 * i + 1-self.num]
      if a < b or a == self.ide_ele:
        a, j, b, k = b, k, a, j
      self.tree[i] = (a, j)

  def update(self, k, x):
    """
    k番目の値をxに更新
    k: index(0-index)
    x: update value
    """
    # 葉の部分が前半に入っている。+= self.numをすることで元になる配列要素に移動
    k += self.num
    self.tree[k] = (x, k - self.num)
    while k > 1:
      # k >> 1 == k // 2 (index k の親の index)
      # k ^ 1 : 末尾を xor する。偶数だったら +1、奇数だったら -1 する。k インデックス(子)の片割れ
      a, i = self.tree[k]
      b, j = self.tree[k ^ 1]
      if a < b:
        a, i, b, j = b, j, a, i

      self.tree[k >> 1] = (a, i)
      k >>= 1

  def query(self, l, r):
    """
    [l, r)のsegfuncしたものを得る
    l: index(0-index)
    r: index(0-index)
    """
    res = (self.ide_ele, 0)

    l += self.num
    r += self.num
    while l < r:
      # l & 1 => l が 奇数 (ペアの右側) だったら 1:
      if l & 1:
        a, i = res
        b, j = self.tree[l]
        if a < b:
          a, i, b, j = b, j, a, i

        res = (a, i)
        l += 1
      # r が奇数 = r-1 が偶数。なので、子のペアの左を見ることになる。
      if r & 1:
        a, i = res
        b, j = self.tree[r - 1]
        if a < b:
          a, i, b, j = b, j, a, i

        res = (a, i)

      # l // 2
      l >>= 1
      r >>= 1
    return res

def resolve():
  # 何回呼ばれるかが変わってくる。
  inf = 10**18+1
  N, M = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    u, v = [int(x)-1 for x in input().split(" ")]
    EDGES[u].append(v)
    EDGES[v].append(u)

  degrees = [len(EDGES[i]) for i in range(N)]
  seg = SegTree([A[i]*len(EDGES[i]) for i in range(N)], segfunc, ide_ele)

  ans = 0
  for i in range(N):
    ans += A[i]*degrees[i]

  for _ in range(N):
    # 消す頂点を決める。
    val, i = seg.query(0, N)
    seg.update(i, 0)
    ans -= val
    for e in EDGES[i]:
      val, _ = seg.query(e, e+1)
      seg.update(e, max(0, val-A[e]))
  print(seg.tree, file=sys.stderr)


  print(ans)

resolve()
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

# tatyam さんの SortedMultiset 
# https://github.com/tatyam-prime/SortedSet
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
# multiset
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

class SortedMultiset(Generic[T]):
  BUCKET_RATIO = 50
  REBUILD_RATIO = 170

  def _build(self, a=None) -> None:
    "Evenly divide `a` into buckets."
    if a is None: a = list(self)
    size = self.size = len(a)
    bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
    self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
  
  def __init__(self, a: Iterable[T] = []) -> None:
    "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
    a = list(a)
    if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
        a = sorted(a)
    self._build(a)

  def __iter__(self) -> Iterator[T]:
    for i in self.a:
      for j in i: yield j

  def __reversed__(self) -> Iterator[T]:
    for i in reversed(self.a):
      for j in reversed(i): yield j
  
  def __len__(self) -> int:
    return self.size
  
  def __repr__(self) -> str:
    return "SortedMultiset" + str(self.a)
  
  def __str__(self) -> str:
    s = str(list(self))
    return "{" + s[1 : len(s) - 1] + "}"

  def _find_bucket(self, x: T) -> List[T]:
    "Find the bucket which should contain x. self must not be empty."
    for a in self.a:
      if x <= a[-1]: return a
    return a

  def __contains__(self, x: T) -> bool:
    if self.size == 0: return False
    a = self._find_bucket(x)
    i = bisect_left(a, x)
    return i != len(a) and a[i] == x

  def count(self, x: T) -> int:
    "Count the number of x."
    return self.index_right(x) - self.index(x)

  def add(self, x: T) -> None:
    "Add an element. / O(√N)"
    if self.size == 0:
      self.a = [[x]]
      self.size = 1
      return
    a = self._find_bucket(x)
    insort(a, x)
    self.size += 1
    if len(a) > len(self.a) * self.REBUILD_RATIO:
      self._build()

  def discard(self, x: T) -> bool:
    "Remove an element and return True if removed. / O(√N)"
    if self.size == 0: return False
    a = self._find_bucket(x)
    i = bisect_left(a, x)
    if i == len(a) or a[i] != x: return False
    a.pop(i)
    self.size -= 1
    if len(a) == 0: self._build()
    return True

  def lt(self, x: T) -> Union[T, None]:
    "Find the largest element < x, or None if it doesn't exist."
    for a in reversed(self.a):
      if a[0] < x:
        return a[bisect_left(a, x) - 1]

  def le(self, x: T) -> Union[T, None]:
    "Find the largest element <= x, or None if it doesn't exist."
    for a in reversed(self.a):
      if a[0] <= x:
        return a[bisect_right(a, x) - 1]

  def gt(self, x: T) -> Union[T, None]:
    "Find the smallest element > x, or None if it doesn't exist."
    for a in self.a:
      if a[-1] > x:
        return a[bisect_right(a, x)]

  def ge(self, x: T) -> Union[T, None]:
    "Find the smallest element >= x, or None if it doesn't exist."
    for a in self.a:
      if a[-1] >= x:
        return a[bisect_left(a, x)]

  def __getitem__(self, x: int) -> T:
    "Return the x-th element, or IndexError if it doesn't exist."
    if x < 0: x += self.size
    if x < 0: raise IndexError
    for a in self.a:
      if x < len(a): return a[x]
      x -= len(a)
    raise IndexError

  def index(self, x: T) -> int:
    "Count the number of elements < x."
    ans = 0
    for a in self.a:
      if a[-1] >= x:
        return ans + bisect_left(a, x)
      ans += len(a)
    return ans

  def index_right(self, x: T) -> int:
    "Count the number of elements <= x."
    ans = 0
    for a in self.a:
      if a[-1] > x:
        return ans + bisect_right(a, x)
      ans += len(a)
    return ans

# takayg1 さんの SegTree https://qiita.com/takayg1/items/c811bd07c21923d7ec69
#####segfunc#####
def segfunc(x, y):
  return x+y
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
  N = int(input())
  C = [int(x)-1 for x in input().split(" ")]
  X = [int(x)-1 for x in input().split(" ")]
  # recent_balles[c]: 今まで見てきたボールの内、c 色のもの。SortedMultiset で管理されている。
  recent_balles = [SortedMultiset([]) for _ in range(N)]

  # seg: 今まで見てきたボールに書かれた数字の個数を記録してある。転倒数を求めるのに使う。
  seg = SegTree([0]*(N+1), segfunc, ide_ele)

  ans = 0
  for i in range(N):
    # 答えに転倒数の一部（X[:i]より左にある X[i] よりも大きな数の個数）を足す。
    ans += seg.query(X[i]+1, N)

    # ↑ で足した値から、色が一緒でコストがかからなかったケースを除外する。
    ans -= recent_balles[C[i]].size - recent_balles[C[i]].index_right(X[i])

    # アップデート
    seg.update(X[i], seg.query(X[i], X[i]+1)+1)
    recent_balles[C[i]].add(X[i])

  print(ans)

resolve()
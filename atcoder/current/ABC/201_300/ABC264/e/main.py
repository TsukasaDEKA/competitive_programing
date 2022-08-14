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


from collections import defaultdict
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
    agg = defaultdict(list)
    for i in range(self.n):
      if self.parents[i] < 0:
        agg[i].append(i)
      else:
        agg[self.parents[i]].append(i)
    return agg

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def resolve():
  # イベントを逆順で処理するのでは？
  N, _, E = map(int, input().split(" "))
  # N 以上の地点を一つの発電所としてみる。
  LINES = [[min(int(x)-1, N) for x in input().split(" ")] for _ in range(E)]
  Q = int(input())
  X = [int(input())-1 for _ in range(Q)]

  # seps: イベントで切断される電線
  seps = set(X)

  # 地点
  union_find = UnionFind(N+1)

  # 構築
  # 切られる予定がない電線を結ぶ => 全てのイベントが完了した状態にする。
  for i in range(E):
    if i in seps: continue
    u, v = LINES[i]
    union_find.union(u, v)

  ans = [0]*Q
  for i in range(Q-1, -1, -1):
    # union_find.size(N) は発電所を含む地点の個数なので、
    # 発電所を答えから省くために -1 する。
    ans[i] = union_find.size(N)-1

    u, v = LINES[X[i]]
    union_find.union(u, v)
  print(*ans, sep="\n")

resolve()
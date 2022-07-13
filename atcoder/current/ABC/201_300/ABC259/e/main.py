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

def resolve():
  from collections import defaultdict

  N = int(input())
  A = [[] for _ in range(N)]

  # max_e[p]: 全ての要素に含まれる p の個数の最大値
  max_e = defaultdict(int)
  for i in range(N):
    M = int(input())
    for _ in range(M):
      p, e = [int(x) for x in input().split(" ")]
      A[i].append((p, e))
      max_e[p] = max(max_e[p], e)

  # max_counts[p]: 全ての要素の p の個数を見て、p の個数が最大値と一致している要素の個数。
  # p の個数が最大値と一致している要素が複数あった場合、その要素を 1 にしても max(e[p]) が変化しないのでその判定に使う。
  max_counts = defaultdict(int)

  # duplicated_max: 最大値が重複している p の集合
  duplicated_max = set()
  for i in range(N):
    for p, m in A[i]:
      if max_e[p] == m:
        max_counts[p] += 1
      if max_counts[p] >= 2:
        duplicated_max.add(p)

  # X = lcm(a_1,...a_N) とする。
  # a_i を 1 に書き換えた時に最小公倍数が X にならない個数を数える。
  ans = 0
  for i in range(N):
    if any(max_e[p] == m and p not in duplicated_max for p, m in A[i]):
      ans += 1

  # ans < N の時、どこかで一回は X が出てきたと考えられるので 1 個追加する。
  if ans < N: ans += 1
  print(ans)

resolve()
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
  inf = 10**18+1
  from collections import deque
  N, M = map(int, input().split(" "))

  EDGES = [[] for _ in range(N)]
  for _ in range(M):
    a, b = [int(x)-1 for x in input().split(" ")]
    EDGES[a].append(b)
    EDGES[b].append(a)
  
  checked = [False]*N

  ans = N*(N-1)//2 - M
  # 自己ループチェック
  parent = [-1]*N
  
  que = deque()
  for i in range(N):
    if checked[i]: continue
    checked[i] = True
    que.append(i)
    right = set()
    right.add(i)
    left = set()

    while que:
      current = que.popleft()
      for e in EDGES[current]:
        if checked[e]:
          # ループチェック
          if current in right and e in right:
            print(0)
            return
          if current in left and e in left:
            print(0)
            return
          continue

        checked[e] = True
        if current in right: left.add(e)
        else: right.add(e)
        parent[e] = current
        que.append(e)

    n = len(right)
    ans -= n*(n-1)//2
    n = len(left)
    ans -= n*(n-1)//2

  print(ans)

resolve()

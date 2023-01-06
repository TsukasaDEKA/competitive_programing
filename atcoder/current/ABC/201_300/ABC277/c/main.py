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
  from collections import defaultdict, deque

  inf = 10**18+1
  N = int(input())
  A_B = [[int(x)-1 for x in input().split(" ")] for _ in range(N)]
  EDGES = defaultdict(list)
  for a, b in A_B:
    EDGES[a].append(b)
    EDGES[b].append(a)

  que = deque([0])
  checked = set([0])
  ans = 0
  while que:
    current = que.popleft()
    for e in EDGES[current]:
      if e in checked: continue
      checked.add(e)
      que.append(e)
      ans = max(ans, e)
  print(ans+1)


resolve()

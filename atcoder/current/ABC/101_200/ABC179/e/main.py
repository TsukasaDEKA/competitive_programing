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

  inf = 10**18+1
  # 必ず周期性がある。
  N, X, M = map(int, input().split(" "))

  if X == 0 or X == 1:
    print(0 if X == 0 else N)
    return

  last_index = defaultdict()
  ans = 0
  agg = [0]*(10**6)

  i = 0
  while N > 0:
    i += 1
    agg[i] = X+agg[i-1]

    if X not in last_index:
      last_index[X] = i
    else:
      length = i - last_index[X]
      v = N//length
      ans += (agg[i] - agg[last_index[X]])*v

      N %= length
      last_index = defaultdict()

    if N <= 0: break

    ans += X
    N -= 1
    X = pow(X, 2)%M

  print(ans)

resolve()

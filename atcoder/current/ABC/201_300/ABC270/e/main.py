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
  from collections import deque

  inf = 10**18+1
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]

  ans = [x for x in A]

  sortedA = sorted([(x, i) for i, x in enumerate(A)])
  sortedA = deque(sortedA)
  less = 0
  zero_count = 0

  while sortedA:
    x, i = sortedA.popleft()

    if x <= less:
      ans[i] = 0
      zero_count += 1
      continue

    if (x-less) * (N-zero_count) <= K:
      K -= (x-less) * (N-zero_count)
      less = x
      ans[i] = 0
      zero_count += 1
    else:
      # 減らす値
      val = K//(N-zero_count)

      less += val
      K -= val*(N-zero_count)
      ans[i] -= less

      # 残ったやつ
      tar = [i]
      while sortedA:
        _, i = sortedA.popleft()
        tar.append(i)
        ans[i] -= less

      # 二個以上残ったケース。
      tar = deque(sorted(tar))
      while tar and K > 0:
        i = tar.popleft()
        ans[i] -= 1
        K -= 1
    # print(ans, less, K)
  print(*ans)

resolve()

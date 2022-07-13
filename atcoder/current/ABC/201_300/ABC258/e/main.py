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
  from itertools import accumulate # 累積和作るやつ
  from bisect import bisect_left

  inf = 10**18+1
  # Wi から始まって Wj で終わる時、 i と j の組み合わせは一意に求まる。
  # ということは周期性がある。
  # 同時に Wi から始めた時に、その箱に何個のジャガイモが入っているのかがわかる。
  N, Q, X = map(int, input().split(" "))
  W = [int(x) for x in input().split(" ")]
  # accW = [0] + list(accumulate(W))
  accW = [0]*(N+1)
  for i in range(1, N+1):
    accW[i] = accW[i-1]+W[i-1]
  
  # i 番目のジャガイモから始めたとき、何番目のジャガイモで終わるかを記録する。
  # 個数も記録する。
  i_to_j = [0]*N
  i_to_count = [0]*N
  for i in range(N):
    x = X
    count = 0
    j = i
    # 残りのジャガイモが x 未満の時、ループする。
    if accW[N] - accW[j] < x:
      count += N - j
      x -= accW[N] - accW[j]
      j = 0
      
      # まだ x 未満の可能性があるので何回かループする。
      if x > accW[N]:
        count += (x//accW[N])*N
        x %= accW[N]

    # 二分探索する。
    if x > 0:
      index = bisect_left(accW, x + accW[j])
      count += index - j
      j = (index)%N

    i_to_j[i] = j
    i_to_count[i] = count
  
  # 閉路を見つける。
  step = [-1]*N
  step[0] = 1
  loop_start  = 0
  loop_length = 0
  current = 0
  step_to_i = [0]
  for _ in range(N):
    next_ = i_to_j[current]
    step_to_i.append(current)
    if step[next_] >= 0:
      loop_length = step[current] - step[next_] + 1
      loop_start = next_
      break
    step[next_] = step[current]+1
    current = next_

  # print(step_to_i, i_to_j, i_to_count)
  L = len(step_to_i)
  for _ in range(Q):
    # K 番目の箱は Wi から始まるのか判定する必要がある。
    K = int(input())
    if K < L:
      i = step_to_i[K]
      print(i_to_count[i])
      continue
    
    # ループの入り口まで動かす。
    # print(K, loop_start, step[loop_start], loop_length)
    k = K
    k -= step[loop_start]
    k %= loop_length
    i = step_to_i[step[loop_start] + k]
    print(i_to_count[i])

resolve()
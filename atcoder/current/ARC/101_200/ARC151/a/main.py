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
  N = int(input())
  S = list(input())
  T = list(input())
  S_1 = deque()
  T_1 = deque()

  for i in range(N):
    if S[i] == T[i]: continue

    if S[i] == "1":
      if T_1:
        T_1.popleft()
      else:
        S_1.append(i)
    else:
      if S_1:
        S_1.popleft()
      else:
        T_1.append(i)

  diff_i = S_1 + T_1
  diff_i.reverse()

  if len(diff_i)%2:
    print(-1)
    return


  ans = ["0"]*N
  for i in range(len(diff_i)//2):
    ans[diff_i[i]] = "1"
  print("".join(ans))

resolve()

import imp
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
  Q = int(input())
  ans = []
  book = defaultdict(int)
  parents = [0]*(Q+1)
  current_index = 0
  top_index = 1
  vals = [0]*(Q+1)

  for _ in range(Q):
    q = input().split(" ")
    if q[0] == "ADD":
      vals[top_index] = int(q[1])
      parents[top_index] = current_index
      current_index = top_index
      top_index += 1

    if q[0] == "DELETE":
      current_index = parents[current_index]

    if q[0] == "SAVE":
      y = int(q[1])
      book[y] = current_index

    if q[0] == "LOAD":
      y = int(q[1])
      current_index = book[y]

    ans.append(vals[current_index] if current_index > 0 else -1)

  print(*ans)
resolve()

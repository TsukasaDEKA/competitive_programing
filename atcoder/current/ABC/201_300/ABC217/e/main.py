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
  from heapq import heappop, heappush
  # ソート済み部分とそうでない部分を別々に管理する。
  Q = int(input())

  p_que = []
  que = deque()

  for _ in range(Q):
    query = [int(x) for x in input().split(" ")]
    if query[0] == 1:
      que.append(query[1])
    elif query[0] == 2:
      print(heappop(p_que) if p_que else que.popleft())
    else:
      while que:
        heappush(p_que, que.popleft())

resolve()
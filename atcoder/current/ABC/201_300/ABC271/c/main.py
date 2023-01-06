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

  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])

  ans = 0
  charge = 0

  A_ = []

  # ダブりは全部捨てる。
  count = set()
  for a in A:
    if a not in count:
      count.add(a)
      A_.append(a)
    else:
      charge += 1

  A = deque(A_)
  while A:
    # print(A, ans, file=sys.stderr)
    # 次の本を読む
    if ans + 1 == A[0]:
      ans += 1
      _ = A.popleft()
      continue

    # 既に読んだ本は捨てる。
    if ans + 1 >= A[0]:
      charge += 1
      _ = A.popleft()
      continue

    # 新しい本を買って読む
    if charge >= 2:
      ans += 1
      charge -= 2
      continue

    # 一冊売って、新しい本を買って読む
    if charge == 1 and len(A) >= 1:
      _ = A.pop()
      charge = 0
      ans += 1
      continue

    # 二冊売って、新しい本を買って読む
    if charge == 0 and len(A) >= 2:
      _ = A.pop()
      _ = A.pop()
      ans += 1
      continue
    
    break

  charge += len(A)
  ans += charge//2

  print(ans)

resolve()

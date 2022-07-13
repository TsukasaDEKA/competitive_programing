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

  # インタラクティブ
  inf = 10**18+1
  N = int(input())
  # 頂点 0 からの距離
  from_0 = [0]*N
  diff_from_0_i = defaultdict(set)
  for i in range(2, N):
    print("? 1 {}".format(i+1))
    l = int(input())
    from_0[i] = l
    diff_from_0_i[l].add(i)

  # 頂点 1 からの距離
  from_1 = [0]*N
  diff_from_1_i = defaultdict(set)
  for i in range(2, N):
    print("? 2 {}".format(i+1))
    l = int(input())
    from_1[i] = l
    diff_from_1_i[l].add(i)

  # 頂点 0 から距離 1 の点が見つからなかったとき
  if 1 not in diff_from_0_i:
    print("! {}".format(1))
    return
  
  # 頂点 1 から距離 1 の点が見つからなかったとき
  if 1 not in diff_from_1_i:
    print("! {}".format(1))
    return

  ans = inf
  for i in range(2, N):
    ans = min(ans, from_0[i]+from_1[i])

  # 距離が 3 の時だけが問題。
  if ans != 3:
    print("! {}".format(ans))
    return

  # 距離が 3 の時、矛盾が発生しないかを確認する。
  # 頂点 1 からの距離が全ての点で 2 の場合、
  count = 0
  for i in range(2, N):
    if from_0[i] == 1 and from_1[i] == 2:
      count += 1

  # 頂点 1 からの距離が 2 かつ頂点 0 からの距離が 1 の点が複数ある場合、答えは 1
  if count > 1:
    print("! {}".format(1))
    return
  
  count = 0
  for i in range(2, N):
    if from_0[i] == 2 and from_1[i] == 1:
      count += 1
  # 頂点 1 からの距離が 1 かつ頂点 0 からの距離が 2 の点が複数ある場合、答えは 1
  if count > 1:
    print("! {}".format(1))
    return

  p_0, p_1 = -1, -1
  for i in range(2, N):
    if from_0[i] == 1 and from_1[i] == 2:
      p_0 = i
    if from_0[i] == 2 and from_1[i] == 1:
      p_1 = i

  print("? {} {}".format(p_0+1, p_1+1))
  l = int(input())
  print("! {}".format(3 if l == 1 else 1))

resolve()
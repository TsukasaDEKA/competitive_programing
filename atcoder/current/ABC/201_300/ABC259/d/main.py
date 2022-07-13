import sys
from tabnanny import check
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
  s_x, s_y, t_x, t_y = map(int, input().split(" "))
  CIRCRES = [[int(x) for x in input().split(" ")] for _ in range(N)]

  # EDGES[i]: 円 i が接している円（円 i から円周上を移動することで移動できる円）
  EDGES = [[] for _ in range(N)]
  for i in range(N-1):
    x_i, y_i, r_i = CIRCRES[i]
    for j in range(i+1, N):
      x_j, y_j, r_j = CIRCRES[j]

      # diff: 円iの中心と円jの中心の距離。
      # 本来は √ をとる必要があるが、誤差が怖いので √ をとらずに扱う。
      diff = pow(x_i-x_j, 2) + pow(y_i-y_j, 2)

      # 片方の円の内側にもう片方円が潜り込むパターン
      if pow(r_j - r_i, 2) > diff: continue

      # 片方の円の内側にもう片方の円が潜り込むパターンを除外した上で、接触判定を行う。
      if pow(r_i + r_j, 2) >= diff:
        EDGES[i].append(j)
        EDGES[j].append(i)

  # starts: 始点が触れている円
  starts = set()
  # goals: 終点が触れている円
  goals = set()
  for i in range(N):
    x_i, y_i, r_i = CIRCRES[i]
    diff = pow(x_i-s_x, 2) + pow(y_i-s_y, 2)
    if diff == pow(r_i, 2):
      starts.add(i)
    
    diff = pow(x_i-t_x, 2) + pow(y_i-t_y, 2)
    if diff == pow(r_i, 2):
      goals.add(i)

  # 始点が触れている円から BFS をやっていって、終点が触れている円にたどり着けたら "Yes"
  deq = deque(starts)
  checked = [i in starts for i in range(N)]
  while deq:
    current = deq.popleft()
    if current in goals:
      print("Yes")
      return
    
    for n in EDGES[current]:
      if checked[n]: continue
      checked[n] = True
      if n in goals:
        print("Yes")
        return
      deq.append(n)

  print("No")

resolve()
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
 
  # N 回ワープするので 3**N の経路がかんがえられる。
  # 経路がどこで途切れるかを予測することは可能か？ => それは難しそう。
  # DP でいけるかも？
  # 結局のところ、「現在どこにいるか」は「1, 2, 3 のワープをそれぞれ何回使ったのか？」に集約される。
  # 何パターンあるか数えてみよう。
  # 仕切りをどこに入れるかの問題なので、302C2 90000 程度しかない。
  # 各ステップで計算を入れても問題ない。
  mod = 998244353
 
  N, M = map(int, input().split(" "))
  X0, Y0, X1, Y1, X2, Y2,  = map(int, input().split(" "))
 
  TO = [(X0, Y0), (X1, Y1), (X2, Y2)]
  BLOCKS = set([tuple(int(x) for x in input().split(" ")) for _ in range(M)]) 

  current = defaultdict(int)
  current[(0, 0)] = 1
 
  for _ in range(N):
    nexts = defaultdict(int)
    for key, value in current.items(): 
      x, y = key
      for dx, dy in TO:
        k = (x+dx, y+dy)
        if k not in BLOCKS:
          nexts[k] += value
          if nexts[k] >= mod: nexts[k]%=mod
 
    current = nexts
 
  ans = 0
  for v in nexts.values():
    ans = (ans+v)%mod
 
  print(ans)
 
resolve()
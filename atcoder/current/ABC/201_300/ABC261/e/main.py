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
  N, C = map(int, input().split(" "))
  # digit: 処理する桁数(二進数)
  digit = 31

  # X を二進数にして桁毎に配列化した状態で持っておく。
  X = [1 if (C>>i)&1 else 0 for i in range(digit)]

  # filters[i][x] := フィルターをかける前に X の i 桁目が x だった時、フィルターをかけた結果が 0 or 1 のどっちになるか
  filters = [[0, 1] for _ in range(digit)]
  for _ in range(N):
    T, A = [int(x) for x in input().split(" ")]
    # A_: 二進数にして桁毎に配列化したもの
    A_ = [1 if (A>>i)&1 else 0 for i in range(digit)]

    # filters を更新する。
    for i in range(digit):
      if T == 1:
        filters[i][0] &= A_[i]
        filters[i][1] &= A_[i]
      elif T == 2:
        filters[i][0] |= A_[i]
        filters[i][1] |= A_[i]
      else:
        filters[i][0] ^= A_[i]
        filters[i][1] ^= A_[i]
    
    # X を更新
    X = [filters[i][X[i]] for i in range(digit)]
    # 二進数の桁毎の配列なので、それを十進数に直して出力する。
    print(sum(X[i]*pow(2, i) for i in range(digit)))

resolve()
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
  from collections import Counter

  # 一回の操作を行なった後に奇数番目と偶数番目の階数の合計は変化しない
  # なので、奇数番目と偶数番目の合計値が一致している区間は操作が可能
  # 偶数番目を正、奇数番目を負にして累積和を取った時に同じ値になる地点から l, r を選ぶと目的を達成できる。
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  accA = list(accumulate([0] + [pow(-1, i+1)*A[i] for i in range(N)]))
  aggA = Counter(accA)
  ans = 0
  for v in aggA.values():
    ans += v*(v-1)//2
  
  print(ans)

resolve()
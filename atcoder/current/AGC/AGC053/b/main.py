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
  from heapq import heappop, heappush

  # 真ん中から二つの山に分けて考える。
  # 高橋君が片方の山から取った後に青木くんは反対の山からカードを取る。
  # つまり、1 ターンで二つの山から一枚ずつ減っていく。
  # 真ん中から順に減っていくことを考える。
  # 青木くんは必ず、山の先頭から取っていくから、山の先頭の両方を高橋くんが取ることはできない。
  # 逆に、高橋くんが上手く操作することで山の先頭の両方を青木くんに取らせることが可能。
  # そうした場合、高橋くんは別のカードを取ることができる。
  # 一度山の先頭の大きい方を取ると仮定する。
  # 取ったと仮定したカードを覚えておいて、もし、それ以降に山の先頭を両方取りたいケースが発生した場合、
  # 取ったと仮定したカードを取らなかったことにする代わりに、そのターンで取りたくなったカードを取ったことにして良い。
  inf = 10**18+1
  N = int(input())
  V = [int(x) for x in input().split(" ")]

  LEFT = [x for x in V[:N][::-1]]
  RIGHT = [x for x in V[N:]]
  taked_card = []
  ans = 0
  for i in range(N):
    l, r = LEFT[i], RIGHT[i]
    ans += max(l, r)
    heappush(taked_card, max(l, r))
    if min(l, r) > taked_card[0]:
      discord = heappop(taked_card)
      heappush(taked_card, min(l, r))
      ans -= discord
      ans += min(l, r)
    
  print(ans)

resolve()
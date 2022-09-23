import sys
from wsgiref.util import request_uri
from xml.etree.ElementTree import TreeBuilder
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
  from itertools import permutations
  from itertools import product

  N, M = map(int, input().split(" "))
  S = [input() for _ in range(N)]
  T = set([input() for _ in range(M)])

  if N == 1:
    if len(S[0]) < 3:
      print(-1)
      return

    print(S[0] if S[0] not in T else -1)
    return

  space = 16 - ((N-1) + sum(len(s) for s in S))

  for p in permutations(list(range(N)), N):
    temp = "_".join([S[i] for i in p])
    if len(temp) >= 3 and temp not in T:
      print(temp)
      return

    for length in range(1, space+1):
      for spe in product(list(range(N-1)), repeat=length):
        # print(spe)
        space_size = [1]*(N-1)
        for i in spe:
          space_size[i] += 1

        temp = ""
        for i in range(N-1):
          temp += S[p[i]]
          temp += "_"*space_size[i]
        temp += S[p[-1]]

        if len(temp) >= 3 and temp not in T:
          print(temp)
          return

  print(-1)

resolve()
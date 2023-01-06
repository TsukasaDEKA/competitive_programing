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
  def factorization(n):
    arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
      if temp%i==0:
        while temp%i==0:
          arr[i]+=1
          temp //= i

    if temp!=1:
      arr[temp] = 1

    if arr.items()==[]:
      arr[n] = 1

    return arr
  

  K = int(input())

  facts = factorization(K)

  p = max(facts.keys()) 
  if p >= 10**6:
    print(p)
    return
  
  for i in range(2, 2*(10**6)+1):
    temp = i
    for k in facts.keys():
      while temp%k == 0:
        temp //= k
        facts[k] -= 1

    keys = list(facts.keys())
    for k in keys:
      if facts[k] <= 0:
        del facts[k]

    if len(facts.keys()) == 0:
      print(i)
      return

resolve()

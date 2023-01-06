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
  def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
      if temp%i==0:
        cnt=0
        while temp%i==0:
          cnt+=1
          temp //= i
        arr.append([i, cnt])

    if temp!=1:
      arr.append([temp, 1])

    if arr==[]:
      arr.append([n, 1])

    return arr
  
  # M == 2 がある以上、答えは 1 or 2
  inf = 10**18+1
  N = int(input())
  A = sorted(list(set([int(x) for x in input().split(" ")])))
  N = len(A)
  if N == 1:
    print(1)
    return

  A = sorted([(A[i+1]-A[i]) for i in range(N-1)])
  if A[0] == 1:
    print(2)
    return

  if len(set(A)) == 1:
    print(1)
    return


  facts = set([k for k, _ in factorization(A[0])])
  for a in A[1:]:
    temp = set()
    for k in facts:
      if a%k == 0:
        temp.add(k)
    facts = temp

  print(2 if len(facts) == 0 else 1)

resolve()
